from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import datetime
app = Flask(__name__)
app.secret_key = 'mykey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'icedb'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT (SELECT COUNT(id) FROM employees) AS `emp`, (SELECT COUNT(id) FROM customers) AS `cust`, (SELECT COUNT(id) FROM ice_cream) AS `ice` , (SELECT COUNT(id) FROM sales) AS `sales`")
    info = cur.fetchone()
    cur.close()
    return render_template('index.html', info=info)

@app.route('/employees', methods=['POST','GET'])
def employees() :
    if request.method=="POST" :
        cur = mysql.connection.cursor()
        search=request.form['search']
        sql="SELECT * FROM `employees` WHERE `name` LIKE '%"+search+"%' OR `address` LIKE '"+search+"'"
        cur.execute(sql)
        data=cur.fetchall()
        cur.close()
        return render_template('employees.html',employees=data)

    cur=mysql.connection.cursor()
    sql="SELECT * FROM `employees`"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return render_template('employees.html',employees=data)

@app.route('/employees/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `employees` (name, address, salary) VALUES (%s, %s, %s)", (name, address, salary))
        mysql.connection.commit()
        return redirect(url_for('employees'))

@app.route('/employees/delete', methods = ['POST','GET'])
def delete():
    if request.method=='POST' :
        idn=request.form['id']
    else :
        return redirect(url_for('employees'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `employees` WHERE id=%s", (idn))
    mysql.connection.commit()
    flash("Ma'lumot muvaffaqiyatli o'chirildi")
    return redirect(url_for('employees'))

@app.route('/employees/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        idn = request.form['id']
        name = request.form['name']
        address = request.form['address']
        salary = request.form['salary']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE `employees` SET name=%s, address=%s, salary=%s
        WHERE id=%s
        """, (name, address, salary, idn))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli yangilandi")
        return redirect(url_for('employees'))

@app.route('/customers', methods=['POST','GET'])
def customers() :
    if request.method=="POST" :
        cur = mysql.connection.cursor()
        search=request.form['search']
        sql="SELECT * FROM `customers` WHERE `name` LIKE '%"+search+"%' OR `shopping` LIKE '"+search+"'"
        cur.execute(sql)
        data=cur.fetchall()
        cur.close()
        return render_template('customers.html',customers=data)
    cur=mysql.connection.cursor()
    sql="SELECT * FROM `customers`"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return render_template('customers.html',customers=data)

@app.route('/customers/insert', methods = ['POST'])
def add():
    if request.method == "POST":
        
        name = request.form['name']
        shopping = request.form['shopping']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `customers` (name, shopping, phone) VALUES (%s, %s, %s)", (name, shopping, phone))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        return redirect(url_for('customers'))

@app.route('/customers/update', methods= ['POST', 'GET'])
def upd():
    if request.method == 'POST':
        idn = request.form['id']
        name = request.form['name']
        shopping = request.form['shopping']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE `customers` SET name=%s, shopping=%s, phone=%s
        WHERE id=%s
        """, (name, shopping, phone, idn))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli yangilandi")
        return redirect(url_for('customers'))

@app.route('/customers/delete', methods = ['POST','GET'])
def dell():
    if request.method=='POST' :
        idn=request.form['id']
    else :
        return redirect(url_for('customers'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `customers` WHERE id=%s", (idn))
    mysql.connection.commit()
    flash("Ma'lumot muvaffaqiyatli o'chirildi")
    return redirect(url_for('customers'))

@app.route('/products', methods=['POST','GET'])
def products() :
    cur=mysql.connection.cursor()
    sql="SELECT * FROM `types`"
    cur.execute(sql)
    types = cur.fetchall()
    
    if request.method=="POST" :
        cur = mysql.connection.cursor()
        search=request.form['search']
        sql="SELECT ice_cream.id, ice_cream.name, ice_cream.price,types.type FROM ice_cream INNER JOIN types ON ice_cream.type_id=types.id WHERE `ice_cream`.`name` LIKE '%"+search+"%' OR `types`.`type` LIKE '%"+search+"%' ORDER BY ice_cream.id ASC"
        cur.execute(sql)
        data=cur.fetchall()
        cur.close()
        return render_template('products.html',products=data,types=types)
    cur=mysql.connection.cursor()
    sql="SELECT ice_cream.id, ice_cream.name, ice_cream.price,types.type FROM ice_cream INNER JOIN types ON ice_cream.type_id=types.id ORDER BY ice_cream.id ASC;"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()    
    return render_template('products.html',products=data,types=types)

@app.route('/products/insert_type', methods = ['POST'])
def add_type():
    if request.method == "POST":
        data = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `types` (id, type) VALUES (%s, %s)", ('NULL',data))
        mysql.connection.commit()
        cur.close()    
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        return redirect(url_for('products'))

@app.route('/products/delete_type', methods = ['POST','GET'])
def dell_type():
    if request.method=='POST' :
        idn=request.form['id']
    else :
        return redirect(url_for('products'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `types` WHERE id=%s", (idn))
    mysql.connection.commit()
    flash("Ma'lumot muvaffaqiyatli o'chirildi")
    return redirect(url_for('products'))

@app.route('/products/update_type', methods= ['POST', 'GET'])
def upd_type():
    if request.method == 'POST':
        idn = request.form['id']
        name = request.form['name']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE `types` SET type=%s
        WHERE id=%s
        """, (name, idn))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli yangilandi")
        return redirect(url_for('products'))

@app.route('/products/insert', methods = ['POST'])
def product_add_type():
    if request.method == "POST":
        name = request.form['name']
        price = request.form['price']
        type_id = request.form['type_id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `ice_cream` (id, name, price, type_id) VALUES (%s, %s,%s, %s)", ('NULL',name, price, type_id))
        mysql.connection.commit()
        cur.close()    
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        return redirect(url_for('products'))

@app.route('/products/update', methods= ['POST', 'GET'])
def product_update():
    if request.method == 'POST':
        idn = request.form['id']
        name = request.form['name']
        price = request.form['price']
        type_id = request.form['type_id']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE `ice_cream` SET name=%s, price=%s, type_id=%s
        WHERE id=%s
        """, (name, price, type_id, idn))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli yangilandi")
        return redirect(url_for('products'))

@app.route('/sales', methods=['POST', 'GET'])
def sales():
    cur = mysql.connection.cursor()   
    cur.execute("SELECT * FROM customers")
    customers = cur.fetchall()
    cur.execute("SELECT * FROM ice_cream")
    products = cur.fetchall()
    if request.method=="POST" :
        q=request.form['search']
        sql="SELECT sales.id, customers.name, ice_cream.name, sales.quantity, sales.price, sales.qqs, sales.total_price, sales.sell_date FROM sales INNER JOIN customers  ON sales.customer_id=customers.id INNER JOIN ice_cream  ON sales.ice_id=ice_cream.id  WHERE `customers`.`name` LIKE '%"+q+"%' OR `ice_cream`.`name` LIKE '%"+q+"%' OR  `sales`.`quantity` LIKE '%"+q+"%'  LIMIT 10"
        cur.execute(sql)
        sales=cur.fetchall()
        cur.close()
        return render_template('sales.html',sales=sales,customers=customers,products=products)
    cur.execute("SELECT sales.id, customers.name, ice_cream.name, sales.quantity, sales.price, sales.qqs, sales.total_price, sales.sell_date  FROM sales INNER JOIN customers  ON sales.customer_id=customers.id INNER JOIN ice_cream  ON sales.ice_id=ice_cream.id ORDER BY sales.id DESC  LIMIT 10")
    sales=cur.fetchall()
    cur.close()
    return render_template('sales.html',sales=sales,customers=customers,products=products)

@app.route('/sales/update', methods= ['POST', 'GET'])
def sales_update():
    if request.method == 'POST':
        idn = request.form['id']
        cust_id = request.form['customer_id']
        ice_id = request.form['ice_id']
        qnt = request.form['quantity']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE `sales` SET customer_id=%s, ice_id=%s, quantity=%s
        WHERE id=%s
        """, (cust_id, ice_id, qnt, idn))
        mysql.connection.commit()
        flash("Ma'lumotlar muvaffaqiyatli yangilandi")
        return redirect(url_for('sales'))

@app.route('/store', methods=['POST','GET'])
def store():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ice_cream")
    products = cur.fetchall()
    if request.method=="POST" :
        q=request.form['search']
        sql="SELECT store.id, ice_cream.name, store.quantity, store.made_date, store.pull_date FROM store INNER JOIN ice_cream ON store.ice_id=ice_cream.id  WHERE `ice_cream`.`name` LIKE '%"+q+"%' OR `store`.`quantity` LIKE '%"+q+"%' OR `store`.`made_date` LIKE '%"+q+"%' OR `store`.`pull_date` LIKE '%"+q+"%' ORDER BY id ASC "
        cur.execute(sql)
        store=cur.fetchall()
        cur.close()
        return render_template('store.html',store=store, products=products)

    cur.execute("SELECT store.id, ice_cream.name, store.quantity, store.made_date, store.pull_date FROM store INNER JOIN ice_cream ON store.ice_id=ice_cream.id ORDER BY id ASC ")
    store=cur.fetchall()
    cur.close()
    return render_template('store.html',store=store, products=products)

@app.route('/store/add', methods = ['POST'])
def store_add():
    if request.method == "POST":
        ice_id=request.form['ice_id']
        qnt=request.form['quantity']
        made=request.form['made_date']
        pull=request.form['pull_date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `store` (id, ice_id,quantity, made_date, pull_date) VALUES (%s, %s, %s, %s, %s)", ('NULL', ice_id,qnt, made,pull))
        mysql.connection.commit()
        cur.close()    
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        return redirect(url_for('store'))


@app.route('/store/update', methods = ['POST'])
def store_upd():
    if request.method == "POST":
        idn=request.form['id']
        ice_id=request.form['ice_id']
        qnt=request.form['quantity']
        made=request.form['made_date']
        pull=request.form['pull_date']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE `store`  SET `ice_id`=%s ,`quantity`=%s, `made_date`=%s, `pull_date`=%s WHERE `id`="+str(idn)+"", (ice_id,qnt, made,pull))
        mysql.connection.commit()
        cur.close()  
        flash("Ma'lumotlar muvaffaqiyatli kiritildi")
        return redirect(url_for('store'))



@app.route('/calc_employee')
def calc_emp():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `employees`")
    employees = cur.fetchall()
    cur.close()
    return render_template('calc_employee.html', employees=employees, data="")

@app.route('/calc_employee/<id>', methods=['GET'])
def calc_emp_get(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `employees` WHERE `id`='"+str(id)+"'")
    data = cur.fetchone()
    cur.execute("SELECT * FROM `employees`")
    employees = cur.fetchall()
    cur.close()
    return render_template('calc_employee.html', employees=employees,data=data)
@app.route('/calc_product')
def calc_pdt():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `ice_cream`")
    ice_cream = cur.fetchall()
    cur.execute("SELECT * FROM `customers`")
    cust = cur.fetchall()
    cur.close()
    return render_template('calc_product.html', ice_cream=ice_cream, data="", customers=cust)

@app.route('/calc_product/<id>', methods=['GET'])
def calc_pdt_get(id):
    today=datetime.date.today()
    today=str(today)
    cur = mysql.connection.cursor()
    sql="SELECT `store`.`id`, `store`.`ice_id`, `ice_cream`.`name`, `types`.`type`, `ice_cream`.`price`, `store`.`made_date` , `store`.`pull_date`, `store`.`quantity` FROM `store` INNER JOIN `ice_cream` ON `store`.`ice_id`=`ice_cream`.`id`  INNER JOIN `types` ON `ice_cream`.`type_id`=`types`.`id` WHERE `store`.`ice_id` = "+id+" AND `store`.`pull_date` > '"+today+"'  AND `store`.`quantity`>0 ORDER BY `store`.`pull_date` ASC"
    cur.execute(sql)
    data = cur.fetchone()
    cur.execute("SELECT * FROM `ice_cream`")
    ice_cream = cur.fetchall()
    cur.execute("SELECT * FROM `customers`")
    cust = cur.fetchall()
    cur.close()
    return render_template('calc_product.html', ice_cream=ice_cream,data=data, customers=cust)

@app.route("/sell", methods=['POST'])
def sell() :
    today=datetime.date.today()
    today=str(today)
    if request.method=="POST" :
        cur = mysql.connection.cursor()
        store_id=request.form['store_id']
        ice_id=request.form['ice_id']
        cust_id=request.form['customer_id']
        qnt=request.form['quantity']
        price=request.form['price']
        qqs=request.form['qqs']
        total=request.form['total_price']
        st_qnt=request.form['st_qnt']
        cur_qnt=int(st_qnt)-int(qnt)
        sql="UPDATE  `store` SET `quantity`='"+str(cur_qnt)+"' WHERE `id`='"+str(store_id)+"'"
        cur.execute(sql)
        mysql.connection.commit()
        cur.execute("INSERT INTO `sales` (id, customer_id,ice_id,quantity,price,qqs,total_price,sell_date) VALUES (%s, %s, %s, %s,%s,%s,%s,%s)", ('NULL', cust_id,ice_id,qnt,price,qqs,total,today))
        mysql.connection.commit()
        cur.close()            
    return redirect(url_for('sales'))

@app.route("/salary", methods=['POST', 'GET']) 
def salary():
    today=datetime.date.today()
    today=str(today)
    if request.method=="POST" :
        idn=request.form['id']
        price=request.form['price']
        cur = mysql.connection.cursor()
        sql="UPDATE `employees` SET `salary`=%s, `salary_date`=%s WHERE `id`=%s"
        cur.execute(sql,(price,today,idn))
        mysql.connection.commit()
        cur.close()            
    return redirect(url_for('employees'))

if __name__ == "__main__":
    app.run(debug=True)