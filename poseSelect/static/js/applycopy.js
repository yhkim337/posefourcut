console.log("1사진변경준비")

function toggleImg(idx) {
  const image = document.querySelector(".modal_content");
  console.log(image.src);
  //const imageUrl = image.src;
  // window.location.href = `http://localhost:8000/fourbyone/image_url=${imageUrl}`;
  window.location.href = `http://localhost:8000/fourbyone/?image_url=${image.src.split('/')[image.src.split('/').length -1]}&index=${idx}`;
  // document.getElementById("img").src = "images/db/fourbyone/sample.png";
  // console.log(document.querySelector(".modal_content"));
}