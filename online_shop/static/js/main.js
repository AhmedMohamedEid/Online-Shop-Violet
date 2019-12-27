/*  ---------------------------------------------------
    Template Name: Violet
    Description: Violet ecommerce Html Template
    Author: Colorlib
    Author URI: https://colorlib.com/
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
		    Product filter
	    --------------------*/
        if ($('#product-list').length > 0) {
            var containerEl = document.querySelector('#product-list');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        appendTo: '.header-section',
        allowParentLinks: true,
        closedSymbol: '<i class="fa fa-angle-right"></i>',
		openedSymbol: '<i class="fa fa-angle-down"></i>'
    });

    /*------------------
		Search model
	--------------------*/
	$('.search-trigger').on('click', function() {
		$('.search-model').fadeIn(400);
	});

	$('.search-close-switch').on('click', function() {
		$('.search-model').fadeOut(400,function(){
			$('#search-input').val('');
		});
	});

    /*------------------
        Carousel Slider
    --------------------*/
     $(".hero-items").owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        items: 1,
        dots: true,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        smartSpeed: 1200,
        autoplayHoverPause: true,
        mouseDrag: false,
        autoplay: false,
    });

    /*------------------
        Carousel Slider
    --------------------*/
    $(".logo-items").owlCarousel({
        loop: true,
		nav: false,
		dots: false,
		margin : 40,
		autoplay: true,
        responsive: {
            0: {
                items: 2
            },
            480: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 5
            }
        }
    });


    /*------------------
        Carousel Slider
    --------------------*/
    $(".product-slider").owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        items: 1,
        dots: true,
        autoplay: true,
    });


    /*------------------
        Magnific Popup
    --------------------*/
    $('.pop-up').magnificPopup({
        type: 'image'
    });

    /*-------------------
		Sort Select
	--------------------- */
    $('.sort').niceSelect();

    /*-------------------
		Cart Select
	--------------------- */
    $('.cart-select').niceSelect();

    /*-------------------
		Quantity change
	--------------------- */
    var proQty = $('.pro-qty');
    proQty.prepend('<span class="dec qtybtn">-</span>');
    proQty.append('<span class="inc qtybtn">+</span>');
    proQty.on('click', '.qtybtn', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find('input').val(newVal);
    });

    /*-------------------
		Radio Btn
	--------------------- */
    $(".shipping-info .cs-item label").on('click', function () {
        $(".shipping-info .cs-item label").removeClass('active');
        $(this).addClass('active');
    });

    $(".checkout-form .diff-addr label").on('click', function () {
        $(this).toggleClass('active');
    });

    $(".payment-method ul li label").on('click', function () {
        $(this).toggleClass('active');
    });

})(jQuery);

var csrftoken = getCookie('csrftoken');

function add2mycart(item_id) {

  console.log(item_id);
  var toAdd = [];

  var item = {
    "id" : item_id,
  }
  toAdd.push(item);

  console.log(toAdd.length);

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  data.append('items', JSON.stringify(toAdd));

  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/add2chart');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      if (data.success)
          alert(`Added item(s) to shopping cart!`)
  };

  // prevernt reload
  return false;
};




function showTotal(data) {
  // console.log(data);
/*
  Data Example:
    {data{
      item_id: 6
      quantity: "4"
      subtotal: 33
      total:
        subtotal__sum: 85
        __proto__: Object
        __proto__: Object
      }
    success: true
    __proto__: Object}
*/
  total = data.data.total.subtotal__sum
  document.querySelector("#total").innerHTML = total;
};

function calc_subtotal(element, price, item_id){

  var item_count = element.value;
  var subtotal = item_count*price;

  // console.log(id.parentElement.nextElementSibling.innerHTML);
  element.parentElement.nextElementSibling.innerHTML = subtotal;
  var toEdit = [];
  var item = {
    "id" : item_id,
    "item_count" : item_count,
    "subtotal" : subtotal
  };
  toEdit.push(item);

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  data.append('items', JSON.stringify(toEdit));


  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/calc_total');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      // if (data.success)
          // showTotal(data);
  };

  // prevernt reload
  return false;
  // alert(item_count+" "+subtotal);
};


function clear_cart(){

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  // data.append('items', JSON.stringify());


  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/clear_cart');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      // if (data.success)
      //     showTotal(data);
  };

  // prevernt reload
  return false;
  // alert(item_count+" "+subtotal);
};


function delete_order(item_id){

  var toDelete = [];
  var item = {
    "id" : item_id,
  };
  toDelete.push(item);

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  data.append('items', JSON.stringify(toDelete));


  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/delete_order');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      // if (data.success)
          // showTotal(data);
  };

  // prevernt reload
  return false;
  // alert(item_count+" "+subtotal);
};


// Get csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
