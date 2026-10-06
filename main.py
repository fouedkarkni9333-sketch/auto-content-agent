import os
import datetime
import google.generativeai as genai

def generate_ai_story():
    print("🤖 جاري الاتصال بالذكاء الاصطناعي لتوليد قصة فريدة وجديدة...")
    
    # استدعاء مفتاح السيرفر السري
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الذكاء الاصطناعي غير موجود في إعدادات جيت هاب!")
        return

    genai.configure(api_key=api_key)
    
    # استخدام نموذج جيميني السريع والمجاني
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "اكتب قصة قصيرة ومبتكرة جداً باللغة العربية حول الابتكار والتكنولوجيا، مع عنوان جذاب ورئيسي، واجعل الأسلوب مشوقاً."
    
    response = model.generate_content(prompt)
    story_text = response.text

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    story_markdown = f"""
# 🚀 قصة ذكية مولدة بالذكاء الاصطناعي
*التاريخ: {date_str} | الوقت: {time_str}*

---

{story_text}

---
*تم توليد هذه القصة بالكامل لحظياً عبر نموذج الذكاء الاصطناعي وسيرفرات جيت هاب.*
"""

    filename = f"ai_story_{date_str.replace('-', '_')}_{time_str.replace('-', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ القصة المولدة بالذكاء الاصطناعي في الملف: {filename}")

if __name__ == "__main__":
    generate_ai_story()
