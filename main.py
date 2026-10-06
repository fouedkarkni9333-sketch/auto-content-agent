import os
import datetime
import time
import google.generativeai as genai

def generate_ai_story():
    print("🤖 جاري الاتصال بالذكاء الاصطناعي لتوليد قصة فريدة...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الذكاء الاصطناعي غير موجود!")
        return

    genai.configure(api_key=api_key)
    
    # استخدام النموذج القياسي المستقر
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "اكتب قصة قصيرة ومبتكرة جداً باللغة العربية حول الابتكار والتكنولوجيا، مع عنوان جذاب، واجعل الأسلوب مشوقاً."
    
    try:
        response = model.generate_content(prompt)
        story_text = response.text
    except Exception as e:
        print(f"حدث خطأ أثناء التوليد (قد يكون بسبب تجاوز الحد المسموح): {e}")
        return

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

    filename = f"ai_story_{date_str.replace('-', '_')}_{time_str.replace('-', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ الملف بنجاح: {filename}")

if __name__ == "__main__":
    generate_ai_story()
