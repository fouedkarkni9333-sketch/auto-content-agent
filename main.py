import os
import time
import datetime
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, DeadlineExceeded

def content_agent():
    print("🤖 جاري تشغيل وكيل المحتوى الذكي (Content Agent)...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الذكاء الاصطناعي غير موجود!")
        return

    genai.configure(api_key=api_key)
    
    model_name = 'models/gemini-3.8-flash'
    print(f"using agent model: {model_name}")
    
    model = genai.GenerativeModel(model_name)
    
    max_retries = 3
    retry_delay = 10
    timeout_limit = 60  # تحديد مهلة زمنية للطلب بالثواني

    # الخطوة 1: توليد الفكرة والمحتوى مباشرة وبأسلوب احترافي لمنع تكرار الاتصالات الطويلة
    prompt = """
    أنت وكيل ذكاء اصطناعي محترف. قم باقتراح عنوان مبتكر ومشيّق، ثم اكتب قصة قصيرة ومبتكرة جداً باللغة العربية حول الابتكار والتكنولوجيا الحديثة.
    """
    
    print("✍️ [الخطوة 1]: الوكيل يقوم بتخطيط وكتابة المحتوى...")
    content_response = None
    for attempt in range(1, max_retries + 1):
        try:
            print(f"محاولة الاتصال (رقم {attempt})...")
            # تمرير مهلة زمنية للطلب لمنع تعليق السيرفر
            content_response = model.generate_content(prompt, request_options={'timeout': timeout_limit})
            break
        except (ResourceExhausted, DeadlineExceeded) as e:
            if attempt < max_retries:
                print(f"⚠️ حدث ضغط أو انقضاء مهلة ({type(e).__name__}). الانتظار لمدة {retry_delay} ثوانٍ...")
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                print("❌ فشلت المحاولات بسبب انتهاء المهلة من السيرفر.")
                raise e

    if not content_response:
        print("❌ لم يتم استلام أي استجابة من الوكيل.")
        return

    story_text = content_response.text

    # الخطوة 2: حفظ المخرجات النهائية مباشرة بدون ضغط إضافي على السيرفر
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    agent_markdown = f"""# 🤖 تقرير وكيل المحتوى الذكي (AI Agent Report)
*التاريخ: {date_str} | الوقت: {time_str}*

---
## المحتوى المُتولد:
{story_text}

---
*تم توليد هذا التقرير وتنفيذ مهام الوكيل تلقائياً عبر سيرفرات جيت هاب.*
"""

    filename = f"agent_report_{date_str}_{time_str.replace(':', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(agent_markdown)
        
    print(f"✅ تم تنفيذ مهام الوكيل بنجاح وحفظ الملف: {filename}")

if __name__ == "__main__":
    content_agent()
