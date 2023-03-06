console.log('연결완료!')
const modal = document.querySelector(".modal");
const sample = document.querySelector(".sample");
const modal_sample = document.querySelector(".modal_content");
const span = document.querySelector(".close");

sample.addEventListener('click', ()=>{
  modalDisplay("block");
  modal_sample.src = sample.src;
});

span.addEventListener('click', ()=>{
  modalDisplay("none");
});
// modal.addEventListener('click', ()=>{
//   modalDisplay("none");
// });
function modalDisplay(text){
  modal.style.display = text;
}