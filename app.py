from flask import Flask, render_template, request
from src.pipeline import predict_pipeline
from src.pipeline.predict_pipeline import predict 
app = Flask (__name__)

@app.route('/')
def home():
    context = {'file_name':'file_name', 'pred':5}
    
    return render_template('index.html',context=context)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image from the request object
    image = request.files['image']
    file_name = image.filename
    # Save the image to disk
    #image.save('uploaded_image.jpg')
    file_path = 'static/uploads/' + image.filename
    image.save('static/uploads/' + image.filename)
    prediction = predict(file_path)
    context = {'file_name':file_name, 'pred':prediction}
    # Print a message to the console
    
    print('Image uploaded successfully!')
    return render_template('predict.html', context=context)


if __name__ == "__main__":
    app.run()
    
