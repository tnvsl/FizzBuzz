from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def suppliers():
    facts = database.get_all_facts()
    return render_template('index.html', facts=facts)

@app.route('/suppliers/<int:supplier_id>')
def products(supplier_id):
    products = database.get_products(supplier_id)
    company_name = database.get_company_name(supplier_id)
    return render_template('products.html', products=products, company_name=company_name)

@app.route('/categories')
def categories():
    categories = database.get_categories()
    return render_template('categories.html', categories=categories)

if __name__ == '__main__':
    app.run()