PImage img;

void setup() {
  fullScreen();
  background(0);
  img = loadImage("/home/pi/sketchbook/proj1/coronavirus.png");
  
}

void draw() {
  noStroke();

  if (int(random(0,2)) == 1) {
    fill(255,0,0);
  } else {
    fill(0,255,0);
  }
  if(frameCount % 20 == 0){
    //background(0);
    float size = random(.5,8);
    image(img,random(displayWidth), random(displayHeight), img.width/size, img.height/size);
  }else if(frameCount % 4 == 0){
    circle(random(displayWidth), random(displayHeight), 80);
  }
  
  if(frameCount % 1500 == 0){
    background(0);
  }
}
