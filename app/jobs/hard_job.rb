class HardJob < ApplicationJob
  class_timeout 300

  rate "1 minute" # every 10 hours
  def dig
    puts "dig"
    {done: "digging"}
  end

  cron "0 */12 * * ? *" # every 12 hours
  def lift
    {done: "lifting"}
  end
end