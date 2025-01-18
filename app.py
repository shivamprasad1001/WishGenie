from flask import Flask, request, jsonify, render_template
from db_config import get_db_connection

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        # Get data from the form
        data = request.form  # Using request.form for form data
        name, occasion, message = data['name'], data['occasion'], data['message']
        
        # Generate the unique link
        unique_link = f"http://localhost:5000/{name}"

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert data into the database
        query = "INSERT INTO wishes (name, occasion, message, link) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, occasion, message, unique_link))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        # Return the generated link as a response
        return jsonify({"link": unique_link})

    # If GET request, render the form
    return render_template('generate_form.html')
@app.route('/<name>')
def wish(name):
    # Connect to the database
    conn = get_db_connection()

    # Use the connection inside a cursor block
    with conn.cursor() as cursor:
        # Query to fetch the data for the given name
        query = "SELECT * FROM wishes WHERE TRIM(name) = %s"
        print(f"Executing query: {query} with name: {name}")  # Debug print
        cursor.execute(query, (name,))
        result = cursor.fetchone()

    # Close the connection after using the cursor
    conn.close()

    print(f"Query result: {result}")  # Debug print

    # If data is found, render the wish page with the retrieved data
    if result:
        return render_template("wish_page.html", name=result[1], occasion=result[2], message=result[3])
    
    # If no data found, show a not found message
    return "Wish not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
