var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
var options = { //지도를 생성할 때 필요한 기본 옵션
    center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
    level: 3 //지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
var ps = new kakao.maps.services.Places();
let data_url = "http://openapi.airport.co.kr/service/rest/AirportParking/airportparkingRT";

let search_btn = document.querySelector(".search-btn");
let search_bar = document.querySelector("#search-bar");
console.log(search_btn);
console.log(search_bar);

search_btn.addEventListener("click", () =>{
    let keyword = search_bar.value;
    if(keyword){
        console.log(keyword + "검색하셨습니다.");
        keywordSearch(keyword);
    } else {
        alert("검색어를 입력해주세요.");
    }
});

search_bar.addEventListener("keyup", () => {
    //keycode 13 = enter key
    if(event.keyCode === 13){
        search_btn.click();
    }
})

function keywordSearch(keyword){
    ps.keywordSearch(keyword, keywordSearchCallBack);
}
function keywordSearchCallBack (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        let center = new kakao.maps.LatLng(data[0].y, data[0].x);
        map.setCenter(center);
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    } 
}

