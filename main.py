import os
import time
import datetime
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, DeadlineExceeded

def generate_ai_story():
    print("🤖 جاري الاتصال بالذكاء الاصطناعي...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الذكاء الاصطناعي غير موجود!")
        return

    genai.configure(api_key=api_key)
    
    # استخدام اسم الموديل القياسي المدعوم بشكل مباشر
    model_name = 'gemini-1.5-flash'
    print(f"using model: {model_name}")
    
    # إعدادات الأمان والطلبات مع تحديد مهلة زمنية للاتصال إذا لزم الأمر
    model = genai.GenerativeModel(model_name)
    prompt = "اكتب قصة قصيرة ومبتكرة جداً باللغة العربية حول الابتكار والتكنولوجيا، مع عنوان جذاب، واجعل الأسلوب مشوقاً."
    
    response = None
    max_retries = 3
    retry_delay = 10  # ثواني الانتظار بين المحاولات عند ضغط الخادم أو انقضاء المهلة

    for attempt in range(1, max_retries + 1):
        try:
            print(f"محاولة التوليد (رقم {attempt})...")
            response = model.generate_content(prompt)
            break
        except (ResourceExhausted, DeadlineExceeded) as e:
            if attempt < max_retries:
                print(f"⚠️ حدث ضغط أو انقضاء مهلة مؤقت ({type(e).__name__}). الانتظار لمدة {retry_delay} ثوانٍ قبل إعادة المحاولة...")
                time.sleep(retry_delay)
                retry_delay *= 2  # مضاعفة وقت الانتظار تدريجياً
            else:
                print("❌ فشلت جميع المحاولات بسبب تجاوز الحد أو انتهاء المهلة. يرجى الانتظار قليلاً ثم إعادة تشغيل الـ Action.")
                raise e

    if not response:
        return

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
