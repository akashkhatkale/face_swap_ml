from flask import *
from image_utils import *
from swapper.image_swapper import *
import insightface
from insightface.app import FaceAnalysis
from firebase_utils import *

app = Flask(__name__)

face_app = FaceAnalysis(name='buffalo_l')
face_app.prepare(ctx_id=0, det_size=(640, 640))
swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False, download_zip=False)


@app.route("/swap", methods=['GET'])
def home():
    data = request.json

    if "user_image" in data.keys() and "target_image" in data.keys():
        user_image = load_image(data["user_image"])
        target_image = load_image(data["target_image"])

        # swap the face, return the file
        face_swap_result = swap_n_show(user_image, target_image, face_app, swapper) 

        # save the file to storage
        img = Image.fromarray(face_swap_result, 'RGB')

        # get the file url
        b = BytesIO()
        img.save(b, 'jpeg')
        image_url = save_image_in_storage(b, data)
        if image_url is not None:
            # refine the image using codeformer
            should_enhance = data["enhance"] if "enhance" in data.keys() else False
            # pass the url to codeformer
            if should_enhance:
                # save this image to firebase too bcoz replicate deletes the image after some time
                image_url = refine_image(image_url)

            return jsonify({
                "url" : image_url
            })
        else:
            return jsonify({
                "error": "Some error occured"
            })
    
    return jsonify({
        "error": "Please provide proper format"
    })



def save_image_in_storage(bytes, data):
    if "user_id" in data.keys() and "id" in data.keys():
        location = "swaps/users/" + data["user_id"] + "/" + data["id"] + ".jpg"
        storage.child(location).put(bytes.getvalue(), "xyz")
        image_url = storage.child("swaps/example.jpg").get_url("xyz")
        return image_url
    else: 
        return None
    


if __name__ == "__main__":
    app.run(debug=False)