require "robo_santa"

describe RoboSanta do
  it "says hello" do
    greet = RoboSanta.new.hello()
    expect(greet).to eq("Hola 😛")
  end
end
