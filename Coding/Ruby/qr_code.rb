require 'rqrcode'
require 'chunky_png'

def display_qr_code(url)
  qr = RQRCode::QRCode.new(url)
  qr.modules.each do |row|
    row.each do |cell|
      print cell ? '██' : '  '
    end
    puts
  end
end

def generate_qr_code_png(url, file_name)
  qr = RQRCode::QRCode.new(url)
  png = qr.as_png(
    resize_gte_to: false,
    resize_exactly_to: false,
    fill: 'white',
    color: 'black',
    size: 120,
    border_modules: 4
  )

  png.save(file_name)
  puts "QR code saved as #{file_name}"
end

puts "Please enter the URL:"
url = gets.chomp

puts "Generating and displaying QR code in terminal..."
display_qr_code(url)

puts "Generating QR code PNG file..."
generate_qr_code_png(url, "qr_code.png")

