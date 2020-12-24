from flask import Flask,request

app = Flask(__name__)

def connection():
    conn=pymysql.connect(host= "127.0.0.1", 
                           user="root", 
                           password="root",
                           db="my_db")
    return conn

@app.route('/register',methods=['POST'])
def register():
    print(request.data)
    data=request.get_json(silent=True)
    username=data['username']
    password=data['password']
    conn=connection()
    cursor=conn.cursor()
    sql='INSERT INTO user(username,password) values(%s,%s)'
    
    val=(username,password)
    cursor.execute(sql,val)
    conn.commit()
    cursor.close()
    conn.close()
    payload=dict(status='success')
    return payload



@app.route('/login',methods=['POST'])
def login():
    print(request.data)
    data=request.get_json(silent=True)
    username=data['username']
    password=data['password']
    conn=connection()
    cursor=conn.cursor()
    sql='SELECT * FROM user WHERE username=%s and password=%s'
    
    val=(username,password)
    cursor.execute(sql,val)
    user_data=cursor.fetchall()
    cursor.close()
    conn.close()
    if user_data:
        payload=dict(status='login success')
        return payload
    else:
        payload=dict(status='login failed')
        return payload 
    
@app.route('/add_address',methods=['POST'])
def add_addr():
    print(request.data)
    data=request.get_json(silent=True)
    street=data['street']
    pincode=data['pincode']
    country=data['country']
    state=data['state']
    phone=data['phone']
    username=data['username']
    
    conn=connection()
    cursor=conn.cursor()
    sql='INSERT INTO address(street,pincode,country,state,phone,username) values(%s,%s,%s,%s,%s,%s)'
    
    val=(street,pincode,country,state,phone,username)
    cursor.execute(sql,val)
    conn.commit()
    cursor.close()
    conn.close()
    payload=dict(status='address added')
    return payload

@app.route('/get_address',methods=['GET'])
def get_addr():
    print(request.data)
    data=request.get_json(silent=True)
    username=data['username']
    conn=connection()
    cursor=conn.cursor()
    sql='SELECT * FROM address WHERE username=%s'
    
    val=(username)
    cursor.execute(sql,val)
    user_data=cursor.fetchall()
    cursor.close()
    conn.close()
    if user_data:
        payload=dict(address=user_data)
        return payload
    else:
        payload=dict(status='user does not exist')
        return payload 

if __name__ == '__main__':
    app.run()