# Simple program to convert Dutch to English

english_dutch = { "last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
"zaag", "first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend", "modern":
"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world ' s leading \
modern composers , Arthur \"Two-Sheds\" Jackson."

# Convert sentence to Dutch (don't worry about punctutation). If a word 
# doesn't exist, then don't translate it.

translation = ""

for word in sentence:
    if word in english_dutch:
        translation += english_dutch[word]
    else:
        translation += word

# print translation

print(translation)