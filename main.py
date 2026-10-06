import os
import datetime
import google.generativeai as genai

def generate_ai_story():
    print("🤖 جاري الاتصال بالذكاء الاصطناعي...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الذكاء الاصطناعي غير موجود!")
        return

    genai.configure(api_key=api_key)
    
    # استخدام النموذج الموصى به والمتاح حالياً
    model_name = 'models/gemini-3.8-flash'
    print(f"using model: {model_name}")
    
    model = genai.GenerativeModel(model_name)
    
    prompt = "اكتب قصة قصيرة ومبتكرة جداً باللغة العربية حول الابتكار والتكنولوجيا، مع عنوان جذاب، واجعل الأسلوب مشوقاً."
    
    response = model.generate_content(prompt)
    story_text = response.text

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    story_markdown = f"""# 🚀 قصة ذكية مولدة بالذكاء الاصطناعي
*التاريخ: {date_str} | الوقت: {time_str}*

---

{story_text}

---
*تم توليد هذه القصة بالكامل لحظياً عبر الذكاء الاصطناعي وسيرفرات جيت هاب.*
"""

    filename = f"story_{date_str}_{time_str.replace(':', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ الملف بنجاح: {filename}")

if __name__ == "__main__":
    generate_ai_story()
