const image_input = document.querySelector("#file");

image_input.addEventListener("change", function(){

    const reader = new FileReader();
    reader.addEventListener("load", function(){
        const uploaded_image = reader.result;
        document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
    });

    reader.readAsDataURL(this.files[0]);
    
})

document.getElementById('form').addEventListener('submit', function(e){
    e.preventDefault();
    const userFile = document.getElementById('file').files[0];

    console.log(userFile.value)
    const formData = new FormData();
    formData.append('file', userFile);
    fetch('http://3.22.114.219:8000/upload_image', {
        method: "POST",
        body: formData,
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)

   document.getElementById("calories").innerHTML = `
   <div id="result" class="card col-5">
  <div class="card-body">
    <p class="card-title">
    
<div class="alert alert-info" role="alert">
    Food: ${data.class_name} <br>
    Estimated Calorie: ${data.estimated_calories}
    </div>
    </p>
  </div>
</div>
   
    `
    })
    .catch(err => console.log(err));
})
