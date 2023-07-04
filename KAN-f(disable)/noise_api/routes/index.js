var express = require('express');
var router = express.Router();
const noise = require('../public/javascripts/mainscript');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.get('/api/noise', function(req, res) {
  res.status(200).json({
    'converted_message': 'test'
  })
})
router.post('/api/noise', function(req, res) {
  tmp = noise.convert_text(req.body.conv_this)
  res.status(200).json({
    'converted_message': tmp
  })
})

module.exports = router;
