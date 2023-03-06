console.log('1연결완료!')
const modal_ = document.querySelector(".modal_");
const H_154_2 = document.querySelector(".H_154_2")
const modal_H_154_2 = document.querySelector(".modal_content");
const span_ = document.querySelector(".close");

H_154_2.addEventListener('click', ()=>{
  modalDisplay("block");
  modal_H_154_2.src= H_154_2.src;
});

span_.addEventListener('click', ()=>{
  modalDisplay("none");
});
// modal.addEventListener('click', ()=>{
//   modalDisplay("none");
// });
function modalDisplay(text){
  modal.style.display = text;
}