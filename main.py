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

    # الخطوة 1 (التخطيط وتوليد الأفكار): اطلب من الوكيل اقتراح 3 مواضيع وتحديد الأفضل
    planning_prompt = """
    أنت وكيل ذكاء اصطناعي متخصص في التكنولوجيا. قم باقتراح 3 عناوين لمواضيع مبتكرة ومستقبلية حول التكنولوجيا الحديثة والذكاء الاصطناعي، واختر الأفضل من بينها لتطويره.
    أعطني عنوان الموضوع المختصر مباشرة مع سبب الاختيار.
    """
    
    print("🧠 [الخطوة 1]: الوكيل يقوم بالتخطيط واختيار الموضوع...")
    plan_response = None
    for attempt in range(1, max_retries + 1):
        try:
            plan_response = model.generate_content(planning_prompt)
            break
        except (ResourceExhausted, DeadlineExceeded) as e:
            if attempt < max_retries:
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                raise e

    if not plan_response:
        print("❌ فشل الوكيل في مرحلة التخطيط.")
        return

    selected_topic = plan_response.text
    print(تم اختيار الموضوع بنجاح:\n{selected_topic[:150]}...\n)

    # الخطوة 2 (التنفيذ والكتابة المعمقة): توليد القصة أو المقال بناءً على اختيار الوكيل
    execution_prompt = f"""
    بناءً على خطة الوكيل والموضوع التالي:
    {selected_topic}
    
    قم بكتابة قصة قصيرة ومبتكرة جداً باللغة العربية حول هذا الموضوع، مع عنوان جذاب، واجعل الأسلوب مشوقاً ومحترفاً.
    """

    print("✍️ [الخطوة 2]: الوكيل يقوم بكتابة وتوليد المحتوى...")
    content_response = None
    for attempt in range(1, max_retries + 1):
        try:
            content_response = model.generate_content(execution_prompt)
            break
        except (ResourceExhausted, DeadlineExceeded) as e:
            if attempt < max_retries:
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                raise e

    if not content_response:
        print("❌ فشل الوكيل في مرحلة توليد المحتوى.")
        return

    story_text = content_response.text

    # الخطوة 3 (المراجعة الذاتية والتحسين): طلب تقييم وتحسين النص للتأكد من خلوه من الأخطاء
    review_prompt = f"""
    قم بمراجعة النص التالي وتصحيح أي أخطاء لغوية أو سياقية، واجعل صياغته أكثر جاذبية واحترافية:
    
    {story_text}
    """

    print("🔍 [الخطوة 3]: الوكيل يقوم بمراجعة وتحسين المحتوى ذاتياً...")
    review_response = None
    try:
        review_response = model.generate_content(review_prompt)
        final_text = review_response.text if review_response else story_text
    except Exception:
        final_text = story_text  # في حال حدوث خطأ بالمراجعة، يتم الاعتماد على النص الأصلي

    # الخطوة 4 (حفظ المخرجات النهائية):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    agent_markdown = f"""# 🤖 تقرير وكيل المحتوى الذكي (AI Agent Report)
*التاريخ: {date_str} | الوقت: {time_str}*

---
## خطة الوكيل واختيار الموضوع:
{selected_topic}

---
## المحتوى النهائي المُراجع:
{final_text}

---
*تم توليد هذا التقرير وتنفيذ دورات الوكيل (التخطيط، التوليد، والمراجعة) تلقائياً عبر سيرفرات جيت هاب.*
"""

    filename = f"agent_report_{date_str}_{time_str.replace(':', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(agent_markdown)
        
    print(f"✅ تم تنفيذ مهام الوكيل بنجاح وحفظ الملف: {filename}")

if __name__ == "__main__":
    content_agent()
