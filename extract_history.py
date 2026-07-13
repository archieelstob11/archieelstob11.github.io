import json
import os

log_file = r"C:\Users\archi\.gemini\antigravity-ide\brain\18a9170b-1f97-4a4d-89a5-03915fa23d84\.system_generated\logs\transcript_full.jsonl"
output_file = "reconstructed_index.txt"

html_lines = {}

with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            if "tool_calls" in data:
                pass
            if "content" in data:
                content = data["content"]
                # Sometimes view_file returns line numbers like `10: <div>`
                if "File Path: `file:///c:/Users/archi/.gemini/antigravity/scratch/restek-website/index.html`" in content:
                    lines = content.split('\n')
                    for l in lines:
                        if ':' in l:
                            parts = l.split(':', 1)
                            if parts[0].strip().isdigit():
                                line_num = int(parts[0].strip())
                                line_content = parts[1][1:] if parts[1].startswith(' ') else parts[1]
                                html_lines[line_num] = line_content
        except Exception as e:
            pass

with open(output_file, "w", encoding="utf-8") as f:
    for i in sorted(html_lines.keys()):
        f.write(f"{i}: {html_lines[i]}\n")

print(f"Extracted {len(html_lines)} lines of index.html")
