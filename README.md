#Slavic Languages Similarity

Outcome of this project is to see the word’s similarity of major Slavic languages. I selected Ukrainian, Bulgarian, Belorussian, Bosnian,  Macedonian, Russian, Serbian, Croatian, Slovakian, Czech, Polish and Slovenian. I haven’t seen similar study published online and I am interested in languages, history and linguistics, so I decided to do this one.

Used technologies: Python, MS Excel, VBA

##Challenges & Solutions

There is no database of words in Slavic languages listed next to each other for comparison
Using Google Translate API with usage of Python to translate list of words to selected languages. I decided to use Swadesh List  as source of words. It is list of 207 basic words.

Eastern and Southern Slavic nations use mainly Cyrillic alphabet. That makes it impossible to compare words
There needs to be done romanisation of the Cyrillic letters to Latin letters. This is done by VBA in MS Excel.

Each Slavic language has it’s own nuances in pronunciation or it’s own letter. That makes the words incomparable
Let’s unify the alphabet and create simplified Slavic alphabet. If the letter will be unique for certain language it needs to be simplified to commonly used letter in other Slavic languages to simplify this case. This makes the words look or sound a bit different than in mother tongue, but it is necessary in order to compare them. Unification will be done via VBA in MS Excel as new Excel function.

It required study of pronunciation of each language for simplification. Other way how to do it is to use some given norm like IPA (International Phonetic Alphabet), but  the approach I chosen is more readable. Especially for person speaking at least one Slavic language.

There is no sufficient built-in function in MS Excel or Python to quantify similarity of strings in percentage
I read about several string comparison methods and spent hours of testing them. None of them was as perfect as I would need, but the simplest and quite well working I would like to mention  Levenshtein Distance and  Damerau–Levenshtein distance. It could be also nice to look at Soundex. I used in the end Fuzzy function I found on vbforums.

##Space for improvement

It would be the best to create function which measures similarity not only by similarity of letter and their position, but also similarity of letters itself, because some words are more similar, because the letter is similar to the missing one.

Words are translated by Google Translator which is still not perfect and it might translate correctly the original word, but if the word had two potential meanings, the output might be translated with the second meaning and then we are comparing two different words.
Words were revised by several native speakers in order to decrease chances of this happening.

It would be great to scale this project to at least 5000 words and this would require quite time consuming participation of native speakers.

##Summary

It was pleasure to do this study, I had chance to see many unseen relations in between languages reflected by geographical and historical development. I am Czech, so it was interesting to see differences and similarities in languages, especially after transcription from Cyrillic alphabet. The most of people won’t even realize the similarity until reading the text which is in most cases readable.

I improved my reading of Cyrillic alphabet during creation of transcription script in MS Excel via VBA.
