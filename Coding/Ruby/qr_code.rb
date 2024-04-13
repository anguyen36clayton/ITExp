require 'rqrcode'

def display_qr_code(url)
  qr = RQRCode::QRCode.new(url)
  qr.modules.each do |row|
    row.each do |cell|
      print cell ? '██' : '  '
    end
    puts
  end
end

puts "Please enter the URL:"
url = gets.chomp

puts "Generating and displaying QR code..."
display_qr_code(url)

