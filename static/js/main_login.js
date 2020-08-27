
(function ($) {
    "use strict";

    /*==================================================================
    [ Validate after type ]*/
    $('.validate-input .input100').each(function () {
        $(this).on('blur', function () {
            if (validate(this) == false) {
                showValidate(this);
            }
            else {
                $(this).parent().addClass('true-validate');
            }
        })
    })

    $('.validate-input-pass .input100').each(function () {
        $(this).on('blur', function () {
            if (validate(this) == false) {
                showValidate(this);
            }
        })
    })


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');
    var input2 = $('.validate-input-pass .input100');

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }
        for (var i = 0; i < input2.length; i++) {
            if (validate(input2[i]) == false) {
                showValidate(input2[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
            $(this).parent().removeClass('true-validate');
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');

        $(thisAlert).append('<span class="btn-hide-validate">&#xf135;</span>')
        $('.btn-hide-validate').each(function () {
            $(this).on('click', function () {
                hideValidate(this);
            });
        });
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
        $(thisAlert).find('.btn-hide-validate').remove();
    }
    // ======================== //
    var password1 = $('#password1');
    var password2 = $('#password2');

    $('.validate-input-pass .input100').each(function () {
        $(this).focus(function () {
            $(this).parent().removeClass('true-validate');
            $(this).parent().removeClass('alert-validate-pass');
        });
    });

    $('#password1').on("keyup", function () {
        if (password1.val().length < 8 && password1.val().length > 0) {
            if (password1.val().trim().match(/^([0-9]+)$/)) {
                $('#message').text('Password Invalid');
            }
            else {
                $('#message').text('Password Weak');
            }
        }
        else if (password1.val().length >= 8) {
            if (password1.val().trim().match(/^([0-9]+)$/)) {
                $('#message').text('Password Invalid');
            }
            else {
                $('#message').text('Password Enough');
            }
        }
        else {
            $('#message').text('');
        }
    });

    $('#password2').on("keyup", function () {
        if (password1.val() == password2.val()) {
            $('#password1').parent().removeClass('alert-validate-pass');
            $('#password2').parent().removeClass('alert-validate-pass');

            $('#password1').parent().addClass('true-validate');
            $('#password2').parent().addClass('true-validate');
        }
    });

    $('.validate-input-pass .input100').each(function () {
        $(this).on('blur', function () {
            $('#message').text('');

            if (password1.val() == password2.val() && password1.val() != 0) {
                $('#password1').parent().removeClass('alert-validate-pass');
                $('#password2').parent().removeClass('alert-validate-pass');

                $('#password1').parent().addClass('true-validate');
                $('#password2').parent().addClass('true-validate');
            }
            else if (password1.val() == 0 || password2.val() == 0) {
                $('#password1').parent().removeClass('alert-validate-pass');
                $('#password2').parent().removeClass('alert-validate-pass');

                $('#password1').parent().removeClass('true-validate');
                $('#password2').parent().removeClass('true-validate');
            }
            else {
                $('#password1').parent().removeClass('true-validate');
                $('#password2').parent().removeClass('true-validate');

                $('#password1').parent().addClass('alert-validate-pass');
                $('#password2').parent().addClass('alert-validate-pass');
            }
        })
    })
})(jQuery);