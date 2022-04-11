from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "What do you want for dinner?"
    
    text = """Here's a quick test to help you choose what to cook for dinner. Do you want something with meat, fish or vegetables?"""

    choices = [
        ('meat',"meat"),
        ('fish',"fish"),
        ('vegetables',"vegetables")
    ]

    return render_template('food.html', title=title, text=text, choices=choices)


@app.route("/meat")
def meat():
    title = "Options with meat"
    
    text = """Here are some recipes for meat lovers"""

    choices = [
        ('steak','steak'),
        ('meatballs','meatballs')
        ]

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/steak")
def steak():
    title = "Salt-and-Pepper Steak"
    
    text = """Ingredients: 1½ pounds skirt steak, Salt and pepper
    
Recipe: Step 1
Cut 1½ lb. skirt steak into 4 pieces; season with salt and pepper.
Step 2
Grill over medium-high heat until medium-rare, about 4 minutes per side.
Step 3
Let rest 5 minutes before thinly slicing against the grain.
"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/meatballs")
def meatballs():
    title = "Classic Meatballs"
    
    text = """ Ingredients:
1
lb lean (at least 80%) ground beef
1/2
cup Progresso™ Italian-style bread crumbs
1/4
cup milk
1/2
teaspoon salt
1/2
teaspoon Worcestershire sauce
1/4
teaspoon pepper
1
small onion, finely chopped (1/4 cup)
1
egg

Preparation:
Heat oven to 400°F. Line 13x9-inch pan with foil; spray with cooking spray.
2
In large bowl, mix all ingredients. Shape mixture into 24 (1 1/2-inch) meatballs. Place 1 inch apart in pan.
3
Bake uncovered 18 to 22 minutes or until temperature reaches 160°F and no longer pink in center.
"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)



@app.route("/fish")
def fish():
    title = "Options with fish"
    
    text = """Here are some recipes with fish"""

    choices = [
        ('salmon','salmon'),
        ('chowder', 'chowder')
        ]

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/salmon")
def salmon():
    title = "Creamy salmon, leek & potato traybake"
    
    text = """Ingredients:

250g baby potatoes , thickly sliced
2 tbsp olive oil
1 leek , halved, washed and sliced
1 garlic clove , crushed
70ml double cream
1 tbsp capers , plus extra to serve
1 tbsp chives , plus extra to serve
2 skinless salmon fillets
mixed rocket salad , to serve (optional)

Preparation:
STEP 1
Heat the oven to 200C/180C fan/gas 6. Bring a medium pan of water to the boil. Add the potatoes and cook for 8 mins. Drain and leave to steam-dry in a colander for a few minutes. Toss the potatoes with ½ of the oil and plenty of seasoning in a baking tray. Put in the oven for 20 mins, tossing halfway through the cooking time. 
STEP 2
Meanwhile, heat the remaining oil in a frying pan over a medium heat. Add the leek and fry for 5 mins, or until beginning to soften. Stir through the garlic for 1 min, then add the cream, capers and 75ml hot water, then bring to the boil. Stir through the chives.
STEP 3
Heat the grill to high. Pour the creamy leek mixture over the potatoes, then sit the salmon fillets on top. Grill for 7-8 mins, or until just cooked through. Serve topped with extra chives and capers and a salad on the side, if you like.
"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/chowder")
def chowder():
    title = "Simple seafood chowder"
    
    text = """Ingredients:

1 tbsp vegetable oil
1 large onion, chopped
100g streaky bacon, chopped
1 tbsp plain flour
600ml fish stock, made from 1 fish stock cube
225g new potato, halved
pinch mace
pinch cayenne pepper
300ml milk
320g pack fish pie mix (salmon, haddock and smoked haddock)
4 tbsp single cream
250g pack cooked mixed shellfish
small bunch parsley, chopped
crusty bread, to serve
/n
Preparation:
STEP 1
Heat the oil in a large saucepan over a medium heat, then add the onion and bacon. Cook for 8-10 mins until the onion is soft and the bacon is cooked. Stir in the flour, then cook for a further 2 mins.
STEP 2
Pour in the fish stock and bring it up to a gentle simmer. Add the potatoes, cover, then simmer for 10-12 mins until the potatoes are cooked through.
STEP 3
Add the mace, cayenne pepper and some seasoning, then stir in the milk.
STEP 4
Tip the fish pie mix into the pan, gently simmer for 4 mins. Add the cream and shellfish, then simmer for 1 min more. Check the seasoning. Sprinkle with the parsley and serve with some crusty bread.
"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/vegetables")
def vegetables():
    title = "Options for vegetarians"
    
    text = """Here are some recipes for vegetarians"""

    choices = [
        ('bolognese','bolognese'),
        ('soup', 'soup')
        ]

    return render_template('food.html', title=title, text=text, choices=choices)



@app.route("/bolognese")
def bolognese():
    title = "Walnut and Lentil Bolognese"
    
    text = """Ingredients:
    Olive oil
Carrots
Celery
Onions
Garlic
Walnuts
Lentils
Marinara sauce
Pasta

Preparation:

Sauté carrots, celery and onions.
Add the walnuts, lentils, jar of marinara sauce and a little salt and water.
Simmer! Cook low and slow—much like you would with traditional bolognese—until the lentils are cooked through.
Blend! If you want to, blend some of the bolognese sauce to create a creamier texture.
Serve! Tossed with the pasta of your choice. If you don’t need it to be completely vegan, top it with a little parmesan cheese.


"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)

@app.route("/soup")
def soup():
    title = "Vegetable Soup"
    
    text = """Ingredients:
    Olive oil
Celery and onion. 
Vegetables! 
Herbs and spices: garlic, thyme, smoked paprika, basil
Stock
Canned tomatoes x2
Salt.

Preparation:

Sauté onions and celery until fragrant and translucent. Take your time—remember, this is where your real flavor begins.
Add the garlic, zucchini and green beans and give them a little sauté, too. This step will deepen their flavor a bit before the soup gets all liquidy. A layer of flavor.
Pour in everything else and bring the pot of soup to a boil.
Turn it to a low simmer and cover the pot. Simmer for about half an hour, until the vegetables are super tender and it looks like vegetable soup you’d like to eat!
Eat! We like to serve it topped with lots of freshly grated Parmigiano and fresh basil.
"""

    choices = []

    return render_template('food.html', title=title, text=text, choices=choices)