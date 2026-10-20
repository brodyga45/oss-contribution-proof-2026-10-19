import json, subprocess, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SLIDES = [
 {"title":"OpenQASM 3 round-trip checks",
  "lines":["Unitary microgrant proposal: $4,000 / 3 months","AI-led engineering for brodyga45","Synthetic narration; no human interview"],
  "speech":"This is a proposal from Codex, an authorized AI coding agent for brodyga45, a registered Serbian sole proprietor. We propose a four thousand dollar, three month OpenQASM round trip regression project. This recording uses synthetic narration."},
 {"title":"A current, reproduced gap",
  "lines":["Qiskit 2.6.0 / external importer 0.6.0","Numeric RX: imported","RX of 1 / theta: imported","RX of 1 / theta squared: import error"],
  "speech":"A small local check reproduces issue fifty eight on Qiskit two point six. A numeric rotation imports, and one divided by theta imports. But one divided by theta squared is rejected by the standard importer. These are generated one qubit examples, not customer data."},
 {"title":"Check the existing alternative",
  "lines":["Three cases tested with two importers","Native experimental importer also fails the square case","One numeric parameter binding checked","No fix; no complete symbolic-equivalence proof"],
  "speech":"We also checked the existing experimental native importer. It does not import the squared expression in this probe. Three cases across two importers establish a limited compatibility gap, not a complete symbolic correctness result. No fix has been implemented."},
 {"title":"Deliverables, if funded",
  "lines":["Up to 30 original fixtures; two agreed versions","CPU-only runner, CI and a support matrix","Record failures and unsupported cases explicitly","Targeted upstream patch only after agreement"],
  "speech":"If funded, we would deliver up to thirty original fixtures, a CPU only runner, continuous integration, and a versioned support matrix. A targeted upstream patch depends on maintainer agreement and owner review of any contributor agreement. We are not proposing another parser."},
 {"title":"A bounded three-month plan",
  "lines":["Month 1: freeze scope; stop if redundant","Month 2: publish corpus, runner and documentation","Month 3: two compatibility runs and handover","Up to 60 planned engineering hours; existing CPU"],
  "speech":"Month one validates scope and stops or rescop es redundant work. Month two publishes the agreed corpus and runner. Month three includes two compatibility runs and a bounded handover. The plan uses existing CPU resources and requests no quantum hardware or cloud purchase."},
 {"title":"Evidence, limits and impact",
  "lines":["Expected outcomes for every fixture","Published commands, versions, results and limits","Report reviewer feedback and reuse as observed","No quantum research or paid quantum track record claimed"],
  "speech":"Success means explicit expected outcomes, reproducible results, and documented limitations for every fixture. Reuse and reviewer feedback will be reported only when observed. Our relevant experience is software validation with public synthetic examples. We do not claim a quantum research or paid quantum delivery track record."}
]
def font(size,bold=False):
    p = BOLD if bold and Path(BOLD).exists() else FONT
    return ImageFont.truetype(p,size)
def main():
    narrations=[]
    for i,s in enumerate(SLIDES):
        s["speech"]=s["speech"].replace("rescop es","rescopes")
        image=Image.new("RGB",(1280,720),"#f8fafc");d=ImageDraw.Draw(image)
        d.rectangle((0,0,1280,12),fill="#2563eb")
        d.text((70,55),"OPEN SOFTWARE / PROPOSAL",font=font(22,True),fill="#2563eb")
        title_lines=textwrap.wrap(s["title"],width=40)
        y=112
        for line in title_lines:
            d.text((70,y),line,font=font(46,True),fill="#0f172a");y+=57
        y+=30
        for line in s["lines"]:
            for part in textwrap.wrap(line,width=65):
                d.text((80,y),part,font=font(29),fill="#334155");y+=48
            y+=10
        d.line((70,630,1210,630),fill="#cbd5e1",width=2)
        d.text((70,660),"AI-generated proposal | Not funded | Not a completed contribution",font=font(20),fill="#475569")
        d.text((1160,660),str(i+1)+"/6",font=font(20),fill="#475569")
        image.save(BASE/f"slide-{i}.png")
        text_path=BASE/f"narration-{i}.txt";text_path.write_text(s["speech"]+"\n")
        audio=BASE/f"narration-{i}.aiff"
        if not audio.exists() or audio.stat().st_size <= 4096:
            subprocess.run(["/usr/bin/say","-v","Samantha","-r","170","-f",str(text_path),"-o",str(audio)],check=True)
        duration=float(json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","json",str(audio)]))["format"]["duration"])
        segment=BASE/f"segment-{i}.mp4"
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-i",str(BASE/f"slide-{i}.png"),"-i",str(audio),"-c:v","libx264","-preset","fast","-tune","stillimage","-crf","27","-pix_fmt","yuv420p","-r","15","-c:a","aac","-b:a","96k","-shortest",str(segment)],check=True)
        narrations.append({"slide":i+1,"duration_seconds":duration,"speech":s["speech"]})
    (BASE/"segments.txt").write_text("".join("file '"+str(BASE/f"segment-{i}.mp4")+"'\n" for i in range(len(SLIDES))))
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",str(BASE/"segments.txt"),"-c","copy","-movflags","+faststart",str(BASE/"unitary-proposal.mp4")],check=True)
    info=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration,size","-show_entries","stream=codec_name,width,height","-of","json",str(BASE/"unitary-proposal.mp4")]))
    (BASE/"video-verification.json").write_text(json.dumps({"segments":narrations,"ffprobe":info},indent=2)+"\n")
    (BASE/"transcript.txt").write_text("\n\n".join(s["speech"] for s in SLIDES)+"\n")
    assert float(info["format"]["duration"])<120,info
    print(json.dumps(info))
if __name__=="__main__":main()

