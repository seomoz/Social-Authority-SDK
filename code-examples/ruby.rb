# Author: Rustam A. Gasanov <rustamagasanov@gmail.com>
# To get this functionality wrapped in gem, check https://github.com/rustamagasanov/social_authority

require 'net/http'
require 'openssl'
require 'base64'
require 'cgi'
require 'json'

module SocialAuthority
  class ResponseError < StandardError; end

  class Api
    attr_reader :options

    def initialize(options)
      @options = { screen_names: [], user_ids: [] }.merge(options)
    end

    def fetch
      uri = URI(generate_request_url)
      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = uri.scheme == 'https'
      request = Net::HTTP::Get.new(uri.request_uri)
      response = http.request(request)

      if response.code == '200'
        JSON.parse(response.body)['_embedded']
      else
        raise ResponseError, response.body
      end
    end

    private
    def generate_request_url
      timestamp = Time.now.to_i + 500

      url = 'https://api.followerwonk.com/social-authority'
      url << '?'
      url << "user_id=#{ options[:user_ids].join(',') };"
      url << "screen_name=#{ options[:screen_names].join(',') };"
      url << "AccessID=#{ options[:access_id] };"
      url << "Timestamp=#{ timestamp };"
      url << "Signature=#{ generate_signature(timestamp) }"
      url
    end

    def generate_signature(timestamp)
      key = options[:secret_key]
      data = "#{ options[:access_id] }\n#{ timestamp }"
      digest = OpenSSL::Digest.new('sha1')
      CGI::escape(Base64.strict_encode64(OpenSSL::HMAC.digest(digest, key, data)))
    end
  end

  def self.fetch(options)
    Api.new(options).fetch
  end
end

p SocialAuthority.fetch({
    access_id:    'YOUR_ACCESS_ID',
    secret_key:   'YOUR_SECRET_KEY',
    user_ids:     ['74594552', '10671602'],
    screen_names: ['Porsche', 'Toyota']
  })
# => [{"_links"=>{"self"=>{"href"=>"/?user_id=14219877"}}, "social_authority"=>"79.55774090527403", "user_id"=>"14219877", "screen_name"=>"Toyota"}, {"_links"=>{"self"=>{"href"=>"/?user_id=57016932"}}, "social_authority"=>"74.10208291651085", "user_id"=>"57016932", "screen_name"=>"Porsche"}, {"_links"=>{"self"=>{"href"=>"/?user_id=10671602"}}, "social_authority"=>"87.26883910802435", "user_id"=>"10671602", "screen_name"=>"PlayStation"}, {"_links"=>{"self"=>{"href"=>"/?user_id=74594552"}}, "social_authority"=>"78.04014172151778", "user_id"=>"74594552", "screen_name"=>"AppStore"}]
