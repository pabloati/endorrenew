import os
import re
import urllib.request
import subprocess

# Paths
brain_dir = '/home/pabloati/.gemini/antigravity-cli/brain/c6a1de53-ed45-4ee8-8033-80d10c1e5249'
md_source = os.path.join(brain_dir, 'project_summary.md')
workspace_dir = '/home/pabloati/HDD1/pablo/cocrea'
images_dir = os.path.join(workspace_dir, 'images')
compiled_md_path = os.path.join(brain_dir, 'project_summary_compiled.md')
pdf_output = os.path.join(workspace_dir, 'project_summary.pdf')

def main():
    print("Starting summary PDF compilation workflow...")
    
    # 1. Create images directory if it doesn't exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        print(f"Created images directory: {images_dir}")

    # 2. Read the source markdown file
    if not os.path.exists(md_source):
        print(f"Error: Source markdown file not found at {md_source}")
        return

    with open(md_source, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. Find and extract Mermaid blocks
    # RegEx to match ```mermaid ... ```
    mermaid_pattern = re.compile(r'```mermaid\n(.*?)\n```', re.DOTALL)
    matches = mermaid_pattern.findall(content)
    print(f"Found {len(matches)} Mermaid diagram(s) to process.")

    # 4. Render each diagram using Kroki API and save as PNG
    for idx, diagram_text in enumerate(matches, 1):
        image_filename = f"diagram_{idx}.png"
        image_path = os.path.join(images_dir, image_filename)
        
        print(f"Rendering diagram {idx}/{len(matches)}...")
        
        # Query Kroki API for PNG
        url = 'https://kroki.io/mermaid/png'
        headers = {
            'Content-Type': 'text/plain',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            req = urllib.request.Request(url, data=diagram_text.encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req) as response:
                png_data = response.read()
                
            with open(image_path, 'wb') as img_f:
                img_f.write(png_data)
            print(f"Saved diagram {idx} to {image_path}")
            
            # Replace in markdown content (escaped index because indices start at 1)
            # Replaces the FIRST occurrence of a mermaid block with the image link
            markdown_image_tag = f"![Mermaid Diagram {idx}](images/{image_filename})"
            content = mermaid_pattern.sub(markdown_image_tag, content, count=1)
            
        except Exception as e:
            print(f"Failed to render diagram {idx}: {e}")
            return

    # 5. Write the compiled markdown to temporary file
    with open(compiled_md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Wrote intermediate markdown to {compiled_md_path}")

    # 6. Compile to PDF using Pandoc and XeLaTeX
    print("Compiling PDF with Pandoc (XeLaTeX engine)...")
    pandoc_cmd = [
        'pandoc',
        compiled_md_path,
        '-o', pdf_output,
        '--pdf-engine=xelatex',
        '-V', 'geometry:margin=1in',
        '-V', 'mainfont=Liberation Sans',
        '-V', 'monofont=DejaVu Sans Mono',
        '--highlight-style=tango'
    ]
    
    try:
        result = subprocess.run(pandoc_cmd, capture_output=True, text=True, check=True)
        print("Success! PDF generated successfully.")
        print(f"PDF saved to: {pdf_output}")
    except subprocess.CalledProcessError as e:
        print("Error compiling PDF with Pandoc:")
        print("Command stdout:", e.stdout)
        print("Command stderr:", e.stderr)

if __name__ == '__main__':
    main()
