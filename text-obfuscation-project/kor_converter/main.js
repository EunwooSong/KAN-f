document
  .getElementById("file-input")
  .addEventListener("change", function (event) {
    var file = event.target.files[0];

    var CHUNK_SIZE = 1024 * 1024; // 1MB

    var reader = new FileReader();
    reader.onload = function (e) {
      var content = e.target.result;
      var jsonData;
      try {
        jsonData = JSON.parse(content);
      } catch (error) {
        console.error("Error parsing JSON:", error);
        return;
      }

      if (jsonData.data && jsonData.data.length > 0) {
        var totalItems = jsonData.data.length;
        var completedItems = 0;

        var progressDiv = document.getElementById("progress");
        progressDiv.innerHTML = "Conversion in progress: 0%";

        var convertedData = [];
        var processDataChunk = function (startIndex) {
          var endIndex = Math.min(startIndex + CHUNK_SIZE, totalItems);
          for (var i = startIndex; i < endIndex; i++) {
            var item = jsonData.data[i];
            var koOriginal = item.ko_original;
            var convKor = convert_text(koOriginal);
            convertedData.push({ ko_original: koOriginal, conv_kor: convKor });

            completedItems++;
            var progressPercent = Math.floor(
              (completedItems / totalItems) * 100
            );
            progressDiv.innerHTML =
              "Conversion in progress: " + progressPercent + "%";
          }

          if (endIndex < totalItems) {
            setTimeout(function () {
              processDataChunk(endIndex);
            }, 0);
          } else {
            var jsonDataNew = { data: convertedData };
            var jsonString = JSON.stringify(jsonDataNew, null, 2);

            var blob = new Blob([jsonString], { type: "application/json" });
            var url = URL.createObjectURL(blob);

            var downloadLink = document.getElementById("save-button");
            downloadLink.href = url;
            downloadLink.download = "TMP.json";
            downloadLink.disabled = false;

            progressDiv.innerHTML = "Conversion completed: 100%";
          }
        };

        processDataChunk(0);
      }
    };

    reader.readAsText(file);
  });
