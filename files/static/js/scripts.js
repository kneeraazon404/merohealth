$("body").on("click", function (e) {
  $('[data-toggle="popover"]').each(function () {
    //the 'is' for buttons that trigger popups
    //the 'has' for icons within a button that triggers a popup
    if (
      !$(this).is(e.target) &&
      $(this).has(e.target).length === 0 &&
      $(".popover").has(e.target).length === 0
    ) {
      $(this).popover("hide");
    }
  });
});


$(".lab_gallery .owl-carousel").owlCarousel({
  loop: true,
  margin: 15,
  autoplay: false,
  dots: false,
  nav: true,
  responsive: {
    0: {
      items: 2,
    },
    600: {
      items: 3,
    },
    1000: {
      items: 5,
    },
  },
});



$("#bs-example-navbar-collapse-1")
  .on("shown.bs.collapse", function () {
    $("#navbar-hamburger").addClass("hidden");
    $("#navbar-close").removeClass("hidden");
  })
  .on("hidden.bs.collapse", function () {
    $("#navbar-hamburger").removeClass("hidden");
    $("#navbar-close").addClass("hidden");
  });

$(".hero .owl-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 1,
    },
    1000: {
      items: 1,
    },
  },
});

$(".reviews-section .owl-carousel").owlCarousel({
  loop: true,
  margin: 15,
  nav: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
  },
});

$(".blog .owl-carousel").owlCarousel({
  loop: true,
  margin: 15,
  nav: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 2,
    },
    1000: {
      items: 3,
    },
  },
});

$(".labs .owl-carousel").owlCarousel({
  loop: true,
  margin: 30,
  nav: true,
  responsive: {
    0: {
      items: 2,
    },
    600: {
      items: 4,
    },
    1000: {
      items: 6,
    },
  },
});


$(".bgtextwrapper .owl-carousel").owlCarousel({
  loop: true,
  margin: 0,
  autoplay: true,
  dots: true,
  nav: false,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 1,
    },
    1000: {
      items: 1,
    },
  },
});



// lab_packages_user_select


$(".lab_packages_user_select .owl-carousel").owlCarousel({
  loop: true,
  margin: 0,
  autoplay: true,
  dots: false,
  autoplayTimeout: 5000,
  autoplayHoverPause: true,
  nav: true,
  navText: ["<i class='las la-angle-left'></i>", "<i class='las la-angle-right'></i>"],
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 1,
    },
    1000: {
      items: 1,
    },
  },
});




$(".btn_add_question").click(function () {
  $(".ask_question_form").slideToggle();
});

$(".orderitem").click(function () {
  $(this).children(".order_full_info").slideToggle(400);
});

$(".upper").click(function () {
  $(this).parent().children(".lower").slideToggle(400);
  $(this).find('.icon').toggleClass("rotateIcon");
});

$('[data-toggle="tooltip"]').tooltip();


$(window).scroll(function (e) {
  var $el = $('.mainbar');
  var isPositionFixed = ($el.css('position') == 'fixed');
  if ($(this).scrollTop() > 5 && !isPositionFixed) {
    $el.addClass('sticky');
  }
  if ($(this).scrollTop() < 5 && isPositionFixed) {
    $el.removeClass('sticky');
  }
});


$(function () {
  $(".popovers").popover({
    html: true,
    trigger: "click",

    content: function () {
      return $(".popover-content").html();
    },
  });
});





$(document).on('click', '[data-toggle="lightbox"]', function (event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});


$('input').focus(function () {
  $(this).parents('.form-group').addClass('focused');
});

$('input').blur(function () {
  var inputValue = $(this).val();
  if (inputValue == "") {
    $(this).removeClass('filled');
    $(this).parents('.form-group').removeClass('focused');
  } else {
    $(this).addClass('filled');
  }
});

$('.panel_heading').click(function () {
  $(this).parent().toggleClass('activePanel');
  $(this).parent().find('.panelBody').slideToggle();

});


$('.otherSlotTrigger').click(function () {
  $(this).parent().parent().find('.customMessage').slideToggle();
})





// $(function () {
//   $('.panelCheckbox').click(function () {
//     var array = [];
//     var parent = $(this).closest('.panelLabel');
//     //check or uncheck sub-checkbox
//     $(parent).find('.subTestItems').prop("checked", $(this).prop("checked"));
//     //push checked sub-checkbox value to array
//     $(parent).find('.subTestItems:checked').each(function () {
//       array.push($(this).val());

//     })
//   });
// })




$('.cancel_trigger').click(function (e) {
  e.preventDefault();
  $(this).parent().parent().parent().find('.formwrapper').slideToggle();
  $(this).parent().parent().parent().find('.messageForm').hide();

});

$('.cancel_message').click(function (e) {
  e.preventDefault();
  $(this).parent().parent().parent().find('.messageForm').slideToggle();
  $(this).parent().parent().parent().find('.formwrapper').hide();

});


$('.btn_decline_trigger').click(function (e) {
  e.preventDefault();
  $(this).parent().parent().parent().find('.declineformwrapper').slideToggle();

});


// checkbox

var checkbox = {
  init: function () {
    var that = this;

    $('.filter-content .filter').each(function () {
      $parent = $(this);

      that.activeChildsByParent($parent);

      $parent.find('input[type="checkbox"]:not(".all")').on('change', function () {
        var $thisParent = $(this).closest('.filter');
        that.activeChildsByParent($thisParent);
      });

      $parent.find('input[type="checkbox"].all').on('change', function () {
        var $thisParent = $(this).closest('.filter');
        that.toggleAllChildsByParent($thisParent);
      })

    });
  },
  toggleAllChildsByParent: function ($parent) {
    var $childs = $parent.find('input[type="checkbox"]:not(.all)'),
      stateAll = $parent.find('input[type="checkbox"].all').prop('checked');

    $childs.prop('checked', stateAll);
    this.activeChildsByParent($parent);
  },
  activeChildsByParent: function ($parent) {
    var $allChilds = $parent.find('input[type="checkbox"].all'),
      total = $parent.find('input[type="checkbox"]:not(.all)').length,
      actives = $parent.find('input[type="checkbox"]:not(.all):checked').length;

    if (actives < total) {
      $allChilds.prop('checked', false);
    } else {
      $allChilds.prop('checked', true);
    }
  }
}

$(document).ready(function () {
  checkbox.init();
})




$('.editIcon').click(function () {
  $(this).parent().parent().find('.formvalue').slideToggle();
  $(this).parent().parent().find('.eidtableFormInput').slideToggle();


})