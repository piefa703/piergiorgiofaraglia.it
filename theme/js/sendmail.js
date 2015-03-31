(function($){
    var userAttributes = '{"personal_information":{"name":"Alex","last_name":"Arriaga","age":25},"extra_information":{"twitter":"alex_arriaga_m","facebook":"alex.arriaga.m","website":"http:\/\/www.alex-arriaga.com\/","programming_languages":"HTML5, CSS3, JavaScript, PHP, Java, C# .NET, AWK, LESS, XML"}}';

    // Function to "simulate" capitalize string
    String.prototype.capitalize = function() {
        return this.charAt(0).toUpperCase() + this.slice(1);
    }

    // Our sending by mail function (reads a PHP JSON object and throws mail client)
    function SendByMail() {
        var body = "-- User Attributes --\r\n\r\n";
        var list = "";

        $.each( userAttributes, function( fkey, fvalue ) {
            list += fkey.toUpperCase().replace("_"," ") + "\n";
            $.each(fvalue, function(skey, svalue){
                list += skey.replace("_"," ").capitalize() + ": " + svalue + "\n";
            });
            list += "\n";
		}); // First level

		body += list;
		// Configure mailto
		var uri = "mailto:piefa703@gmail.com?subject=";
		    uri += encodeURIComponent(document.title);
		    uri += "&body=";
		    uri += encodeURIComponent(body);
		    window.location.href = uri;
		}

		$(document).on('ready', function(){
			$("#sendByEmail").on('click', function(){
				SendByMail();
			});
		});
	})(jQuery);