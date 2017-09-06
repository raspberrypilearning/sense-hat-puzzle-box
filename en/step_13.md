## Set the combination

Now you need to specify the combination - the sequence of angles that will successfully unlock this lock.

+ In your `Locks` section, create two empty lists, one called `combination` and one called `complete`.

[[[generic-python-create-list]]]

+ Inside the `combination` list, add a sequence of angles the player must follow by rotating the Sense HAT. Make sure you only use the angles `0`, `90`, `180` and `270` as these are the ones you can detect.

For example you might choose the following:

```python
combination = [0,180,90,0,270]
complete = []
```

The second list, `complete`, will be used to store the completed steps of the combination: each time the user gets a step correct, that number gets moved to the complete list.

![Item moving](images/list-move.png)

When the code list is empty then the combination has been completed and the lock is unlocked.
