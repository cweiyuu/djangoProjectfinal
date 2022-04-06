$.ajax({
    url: "http://127.0.0.1:8000/api/ProductModel/",
    method: "GET",
    dataType: 'json',
    success: function (data) {
        console.log('---success---');
        console.log(data);
        $(".content").empty();
        for (i in data) {
            console.log(i);
            let sBox = `
            <a href="#">
                <div class="box">
                <img src="img_file/p0${i}.jpg" alt="Card image">
                    <div >
                        <h5>${data[i].name}</h5>
                        <p>${data[i].description}</p>   
                        <p>${data[i].price}元</p>
                        <button class="btn btn-primary float-right" style="margin-bottom:1em">加入購物車</button>
                    </div>
                </div>
            </a>
            `;
            $(".content").append(sBox);
        }
        // $.each(data, function (index) {
    }
});