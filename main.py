import os
import datetime
import random

def generate_story():
    print("📖 بدء تشغيل نظام توليد القصص مع الصور التعبيرية...")
    
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    
    # بنك القصص مع إضافة رابط صورة تعبيرية مجانية لكل قصة
    story_bank = [
        {
            "title": "حكاية العقل البشري والابتكار",
            "genre": "قصة تحفيزية",
            "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=60",
            "content": "في قرية هادئة، كان فني شاب يقضي لياليه وسط الأجهزة. بالصبر والأدوات البسيطة، استطاع أن يصنع أول نظام أتمتة يغير حياته."
        },
        {
            "title": "سر الخوارزمية في عمق السيرفرات",
            "genre": "خيال علمي",
            "image_url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=60",
            "content": "في عالم رقمي يتسارع فيه الزمن، كانت الأكواد تعمل بصمت لترتيب المعرفة وصنع إمبراطوريات رقمية كاملة."
        },
        {
            "title": "ملحمة الصيانة الكبرى",
            "genre": "دراما واقعية",
            "image_url": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=60",
            "content": "توقف خط الإنتاج فجأة وسط الليل، وبخبرة هادئة وأدوات بسيطة استطاع الفني إعادة الحياة للآلة في دقائق معدودة."
        }
    ]
    
    selected_story = random.choice(story_bank)
    
    # هيكل الملف مع الصورة التعبيرية في الأعلى
    story_markdown = f"""
# 📚 {selected_story['title']}
*التاريخ: {date_str} | التصنيف: {selected_story['genre']}*

![صورة تعبيرية]({selected_story['image_url']})

---

{selected_story['content']}

---
*تم توليد هذه القصة والصورة التعبيرية تلقائياً عبر بايثون وسيرفرات جيت هاب.*
"""

    filename = f"story_{date_str.replace('-', '_')}_{time_str.replace('-', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ القصة مع الصورة في الملف: {filename}")

if __name__ == "__main__":
    generate_story()
