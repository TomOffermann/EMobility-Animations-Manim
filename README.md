# EMobility-Animations-Manim
Animations created with Manim for my graduation exam presentation

## Setup:
Have Python installed. Then:

<pre>
<code >pip install manim</code>
</pre>
For motors:
<pre>
<code >cd ./motors</code>
</pre>
For storage solutions: 
<pre>
<code >cd ./storage_concepts</code>
</pre>
Render Animation: 
<pre>
<code >manim %flags% %file_name% %scene_name%</code>
</pre>
You can find the scene_name as the name of classes in the python animation files. <br/>
<br/>
* Flags: For more information look in Manim-Docs 
  * -q[quality] and -pq[quality], -q for normal render, -pq for render with instant-play of video<br/>
  * with quality = (l,m,h,k) for low, medium, high and ultra
____
Example: 
<pre>
<code >cd ./motors && manim -qh dc_motor.py DCMotor</code>
</pre>


## Some Previews:

## Videos:
____

https://user-images.githubusercontent.com/71230696/151456958-23418e0d-9001-4033-b840-4742157abe60.mp4
____

https://user-images.githubusercontent.com/71230696/151457465-8916e419-7e54-49fe-a1bd-ddc0182243b0.mp4
____

## Images:
____
### Gleichstrommotor:
![DCMotor_ManimCE_v0 14 0](https://user-images.githubusercontent.com/71230696/151456485-b47cf48a-0efd-4e4c-b812-888f102cc21f.png)

----
### Einfacher E-Motor Aufbau:
![SimpleMotor_ManimCE_v0 14 0](https://user-images.githubusercontent.com/71230696/151456526-351be468-6afc-4ac2-93be-c8fcfeba7442.png)

----
### Dreiphasiger Strom:
![ExampleSineWaves_ManimCE_v0 14 0](https://user-images.githubusercontent.com/71230696/151456361-dd29e03f-e518-437d-aaa1-768de834e57a.png)

----
### Wechselstrommotor:
![ACMotor_ManimCE_v0 14 0](https://user-images.githubusercontent.com/71230696/151456327-5509bf3b-396e-4193-bb87-706202e81a92.png)
