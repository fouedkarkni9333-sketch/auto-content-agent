import os
import datetime
import random

def generate_story():
    print("📖 بدء تشغيل نظام توليد القصص والحكايات...")
    
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
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
        }
    ]
    
    selected_story = random.choice(story_bank)
    
    story_markdown = f"""
# 📚 {selected_story['title']}
*التاريخ: {today} | التصنيف: {selected_story['genre']}*

---

{selected_story['content']}

---
*تم توليد هذه القصة تلقائياً عبر بايثون.*
"""

    filename = f"story_{today.replace('-', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story_markdown)
        
    print(f"تم حفظ القصة في: {filename}")

if __name__ == "__main__":
    generate_story()
