#%%
import pandas as pd

#%%
csv_file = r"JEE-2025 - jee_pdf_content (1).csv"

#%%

def generate_html_from_csv(csv_path=csv_file , output_path=r"jee-2025.html"):
    df = pd.read_csv(csv_path)

    html_blocks = []
    for idx, row in df.iterrows():
        q_num = row.get("question_number", f"Question {idx+1}")
        img_src = row.get("image_path", "")
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
            table {{
                width: 90%;
            margin: 0 auto 50px;
            border-collapse: collapse;
            text-align: center;
            font-size: 16px;
            }}      

            th, td {{
                border: 1px solid #333;
                padding: 10px 14px;
            }}

            th {{
                background-color: #f2f2f2;
            }}

            caption {{
                caption-side: top;
                font-weight: bold;
                font-size: 20px;
                margin-bottom: 15px;
            }}
        </style>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script type="text/javascript" id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        <h1 style="text-align: center; margin-bottom: 40px;"><u>NEET-2025 Code-48 AI Solutions</u></h1>
        <table>
        <div style="text-align: center; margin-bottom: 30px;">
            <h2>Accuracy Summary</h2>
        </div>
        <thead>
            <tr>
                <th>Subject</th>
                <th>Correct</th>
                <th>Incorrect</th>
                <th>Question Numbers</th>
                <th>Total</th>
                <th>Accuracy</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Mathematics</td>
                <td>24</td>
                <td>1</td>
                <td>15</td>
                <td>25</td>
                <td>96%</td>
            </tr>
            <tr>
                <td>Chemistry</td>
                <td>24</td>
                <td>1</td>
                <td>74</td>
                <td>25</td>
                <td>96%</td>
            </tr>
            <tr>
                <td>Physics</td>
                <td>23</td>
                <td>2</td>
                <td>26, 49</td>
                <td>25</td>
                <td>92%</td>
            </tr>
            <tr>
                <td><strong>Total</strong></td>
                <td><strong>71</strong></td>
                <td><strong>4</strong></td>
                <td></td>
                <td><strong>75</strong></td>
                <td><strong>94.7%</strong></td>
            </tr>
        </tbody>
    </table>
    <div style="text-align: center; margin-bottom: 30px;">
        <h2>Incorrectly Answered Questions</h2>
    </div>

    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 60px;">
        <div>
            <p style="text-align: center;">Q15</p>
            <img src="jee_images/15.png" alt="Question 41" style="max-width: 400px; border: 1px solid #ccc; padding: 5px;">
        </div>
        <div>
            <p style="text-align: center;">Q26</p>
            <img src="jee_images/26.png" alt="Question 74" style="max-width: 400px; border: 1px solid #ccc; padding: 5px;">
        </div>
        <div>
            <p style="text-align: center;">Q49</p>
            <img src="jee_images/49.png" alt="Question 90" style="max-width: 400px; border: 1px solid #ccc; padding: 5px;">
        </div>
        <div>
            <p style="text-align: center;">Q74</p>
            <img src="jee_images/74.png" alt="Question 141" style="max-width: 400px; border: 1px solid #ccc; padding: 5px;">
        </div>
        
    </div>
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

df['image_path'] = df['image_path'].str.replace(
    "C:\\Users\\Abcom\\Desktop\\JEE_evaluation\\Jee_images_set_1\\",
    "jee_images/",
    regex=False
)
df.head()

#%%

# df[df['image_path'].str.contains("C:\Users\Abcom\Desktop\JEE_evaluation\Jee_images_set_1\")]

#%%

df.to_csv("JEE-2025 - jee_pdf_content (1).csv", index=False)
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
