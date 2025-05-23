#%%
import pandas as pd

#%%
csv_file = r"C:\Users\Abcom\Desktop\JEE_evaluation\JEE-2025 - jee_pdf_content.csv"

#%%

def generate_html_from_csv(csv_path=csv_file , output_path=r"C:\Users\Abcom\Desktop\JEE_evaluation\questions.html"):
    df = pd.read_csv(csv_path)

    html_blocks = []
    for idx, row in df.iterrows():
        q_num = row.get("question_number", f"Question {idx+1}")
        img_src = row.get("question_url", "")
        correct_option = row.get("correct_answer", "N/A")
        solution = row.get("solution", "")

        block = f"""
        <div style="margin: 40px 0; padding: 20px; border-bottom: 1px solid #ccc;">
            <h2>Question {q_num}</h2>
            <div>
                <img src="{img_src}" alt="Question Image" style="max-width: 100%; height: auto;" />
            </div>
            <p><strong>Correct Option:</strong> {correct_option}</p>
            <div>
                <strong>Solution:</strong>
                <p>{solution}</p>
            </div>
        </div>
        """
        html_blocks.append(block)
        # <div class="question-page">
        #     <h2>Question {q_num}</h2>
        #     <div>
        #         <img src="{img_src}" alt="Question Image" style="max-width: 100%; height: auto;" />
        #     </div>
        #     <p><strong>Correct Option:</strong> {correct_option}</p>
        #     <div>
        #         <strong>Solution:</strong>
        #         <p>{solution}</p>
        #     </div>
        # </div>

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Questions Viewer</title>
        <style>
            @page {{
                size: A4;
                margin: 20mm;
            }}

            body {{
                font-family: sans-serif;
                margin: 0;
                padding: 0;
            }}

            .title {{
                text-align: center;
                font-size: 24px;
                margin: 40px 0;
            }}

            .question-page {{
                width: 210mm;
                height: 297mm;
                padding: 20mm;
                box-sizing: border-box;
                page-break-after: always;
                overflow: hidden;
            }}

            .question-page:last-child {{
                page-break-after: auto;
            }}

            img {{
                max-width: 100%;
                height: auto;
            }}

            h2 {{
                margin-top: 0;
            }}
        </style>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script type="text/javascript" id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        <h1 style="text-align: center; margin-bottom: 40px;">JEE-2025 [ 22-01-2025 (shift 1) ]</h1>
        {''.join(html_blocks)}
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"✅ HTML generated: {output_path}")

#%%

csv_to_html = generate_html_from_csv(csv_file)

#%%

df = pd.read_csv(csv_file)
df.head()

#%%

df['question_url'] = df['question_url'].str.replace(
    r"C:/Users/Abcom/Desktop/JEE_evaluation/Jee_images_set_1",
    r"question/",
    regex=False
)
df.head()

#%%

# df[df['question_url'].str.contains("/C:/Users/Abcom/Downloads/question/")]

#%%

df.to_csv("exam_neet_sample.csv", index=False)
#%%

csv_file.to_csv("exam_neet_sample.csv", index=False)

#%%


#%%

# #%%

# df = pd.read_csv(csv_file)
# df.head()
# # %%
# df.columns
# # %%


# df.head()
# # %%


# # %%

# df['question_url'] = df['question_url']


# # # %%

# # df.head()
# # # %%
