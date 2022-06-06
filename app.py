from flask import Flask, render_template, request
from query import Query
from mydb import MyDB

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        user_query = request.form.get('query_input')
        user_query = user_query.lower()
        if user_query == '':
            return render_template('search.html', error='Please enter a query')
        Q = Query()
        results = Q.phrase_query(user_query)
        print(results)
        db = MyDB()
        urls = []
        for file in results:
            urls.append(db.get(file).decode('utf-8'))
        print(urls)
        return render_template('search.html', urls=urls, query=user_query)        
    return render_template('search.html')
    
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
    print("Server is running at http://0.0.0.0:5000")