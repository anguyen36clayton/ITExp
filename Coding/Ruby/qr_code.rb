require 'rqrcode'
require 'rqrcode_png'

def generate_qr_code(url, filename)
  qr = RQRCode::QRCode.new(url)
  png = qr.as_png(
    resize_gte_to: false,
    resize_exactly_to: false,
    fill: 'white',
    color: 'black',
    size: 120
  )
  IO.binwrite(filename, png.to_s)
  puts "QR code generated successfully as '#{filename}'."
end

puts "Please enter the URL:"
url = gets.chomp

puts "Generating QR code..."
generate_qr_code(url, 'qr_code.png')

