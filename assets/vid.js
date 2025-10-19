const boxes = [
  { sel: ".box1", audio: "#Ancient", video: ".bg_videox" },
  { sel: ".box2", audio: "#Rift", video: ".bg_videoy" },
  { sel: ".box3", audio: "#Blacklight", video: ".bg_videoz" },
];

boxes.forEach(({ sel, audio, video }) => {
  const audioEl = $(audio)[0];
  $(sel).on("mouseenter", function () {
    audioEl.play();
    $(".bg_videox, .bg_videoy, .bg_videoz").hide();
    $(video).show();
  });
  $(sel).on("mouseleave", function () {
    audioEl.pause();
    $(video).hide();
  });
});