# Ludwig Wittgenstein's Philosophy
python3 module

## Start instructions
- Clone this repository: `git clone https://github.com/Khazbs/ludwig`
- Go to its folder: `cd ludwig`
- Open either:
  - **start.sh** in your **shell** (for **bash** you can write `. start.sh`)
  - **ludwig.py** in your **python3** interpreter's **i**nteractive mode: `python3 -i ludwig.py`
- You should now be notified that `--- Ludwig module has been loaded ---` and be prompted to write some code by your **python3** interpreter: `>>>`

## Simple test cases
- Try creating some simple **objects**:
`dog = Object()`;
`cat = Object()`.
- Try creating **relations** between them via **interactions**:
`dog_barks_at_cat = Relation(dog, cat, Interaction('barks at'))`;
`cat_runs_away_from_dog = Relation(cat, dog, Interaction('runs away from'))`.
- Try creating an **event** based on them:
`dog_scares_cat_off = Event([dog_barks_at_cat, cat_runs_away_from_dog])`.
- Try checking that the **event** is now stated in both **objects' forms**:
`dog_scares_cat_off in dog.form`;
`dog_scares_cat_off in cat.form`.
- Try creating a **fact** that claims that this **event** happens:
`dog_and_cat_fact = Fact([dog_scares_cat_off])`.
- Try creating a **thought** about this **fact**:
`thought_about_dog_and_cat = Thought(dog_and_cat_fact)`.
- Try creating a **world** based on the **fact**:
`world = World([dog_and_cat_fact])`. Of course, a real **world** would have a lot more **facts**, but this is just an example.
- Try checking that both **objects** form the **substance** of this **world**:
`dog in world.substance`;
`cat in world.substance`.
- Try creating a **picture** of this **world** and checking if it is a **correct representation** of it:
`world_picture = Picture(world)`; `world_picture <= world`.
- Try defining **symbols** for **objects** that you have:
`symbols = [Symbol(dog, 'dog'), Symbol(cat, 'cat')]`.
- Try making a **sentence** about your **world** using your **symbols** and also checking if it is **correct**:
`world_sentence = Sentence(world, symbols)`; `world_sentence <= world`.
- Try getting a **textual representation** of your sentence:
`print(world_sentence)`.

## Philosophical questions
- Can a **picture** be a **picture of itself**?
  - **No**, it cannot: if `type(picture)` is `Picture`, `type(picture.meaning)` will never be `Picture`.
- If **The Pure Thought** refers to the simplest thought, the existence of which proves its verity, is it possible to **think The Pure Thought**?
  - **No**, it is impossible: `Picture(Thought())` fails with an error.
