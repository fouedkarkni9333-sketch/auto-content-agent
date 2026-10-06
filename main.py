import os
import datetime
import random

def generate_story():
    print("📖 بدء تشغيل نظام توليد القصص والحكايات...")
    
    # الحصول على التاريخ والوقت الحالي بدقة لتوليد اسم فريد لكل قصة
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    story_bank = [
        {
            "title": "حكاية العقل البشري والابتكار",
            "genre": "قصة تحفيزية",
            "content": "في قرية هادئة، كان فني شاب يقضي لياليه وسط الأجهزة. بالصبر والأدوات البسيطة، استطاع أن يصنع أول نظام أتمتة يغير حياته."
        },
        {
            "title": "سر الخوارزمية في عمق السيرفرات",
            "genre": "خيال علمي",
            "content": "في عالم رقمي يتسارع فيه الزمن، كانت الأكواد تعمل بصمت لترتيب المعرفة وصنع إمبراطوريات رقمية كاملة."
        },
        {
            "title": "ملحمة الصيانة الكبرى",
            "genre": "دراما واقعية",
            "content": "توقف خط الإنتاج فجأة وسط الليل، وبخبرة هادئة وأدوات بسيطة استطاع الفني إعادة الحياة للآلة في دقائق معدودة."
        }
    ]
    
    selected_story = random.choice(story_bank)
    
    story_markdown = f"""
# 📚 {selected_story['title']}
*التاريخ: {date_str} | التصنيف: {selected_story['genre']}*

---

{selected_story['content']}

---
*تم توليد هذه القصة تلقائياً عبر بايثون وسيرفرات جيت هاب.*
"""

    # تسمية الملف باسم فريد يعتمد على التاريخ والوقت لضمان ظهور ملف جديد في كل تشغيل
    filename = f"story_{date_str.replace('-', '_')}_{time_str.replace('-', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ القصة في الملف الجديد: {filename}")

if __name__ == "__main__":
    generate_story()
