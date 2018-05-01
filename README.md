# spikingneurons
Simulation of neurons according to Eugene M. Izhikevich's "Simple Model of Spiking Neurons" (2003)

### Install
You'll need [python3](https://www.python.org/download/releases/3.0/) and [matplotlib](https://matplotlib.org/users/installing.html)

### Usage
You'll generally want to use this from Python's shell, so start it up from the folder you cloned this to:
```python3```

Next, import the file:
```import model```

Let's create a new neuron with standard settings:
```neuron = model.Neuron()```

Now we can run the simulation on the neuron. If everything worked, a window with the graph should pop up:
```neuron.Simulate(steps=2000, I=[10])```

To get different results, tamper with different neurons. They got a, b, c and d as parameters. Also, changing I in Simulate will get you something else.
