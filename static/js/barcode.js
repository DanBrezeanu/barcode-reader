jQuery(document).ready(function($) {
  $(document).ready(function() {
      // $("#file-selector").on("change", function() {
      //     $.getElementById("photo-form").form.submit();
      // })

      $("#save-button").click(function () {
          $.getJSON(self.location.host + "barcode/save-photo/", function(data) {
              if (data.response) {
                  $.each(data.barcodes, function(value) {
                      console.log('>>>  ' + value.name + ': ' + value.value)
                  })
              }
          })
      })
  })
})
