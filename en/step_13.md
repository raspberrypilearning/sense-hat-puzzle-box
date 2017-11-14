## Set the combination

Now you need to specify the combination — the sequence of angles that will successfully unlock this lock.

+ In your **Locks** section below the code for your other locks, create two empty lists: one called `combination` and one called `complete`.

[[[generic-python-create-list]]]

+ Inside the `combination` list, add a sequence of angles at which the user must position the Sense HAT by rotating it. Make sure you only use the angles `0`, `90`, `180`, and `270`, as these are the ones you can detect.

For example, you might choose the following:

```python
combination = [0,180,90,0,270]
complete = []
```

The `complete` list will be used to store the completed steps of the combination: each time the user gets an angle correct, that item gets moved to the `complete` list from the `combination` list.

![Item moving](images/list-move.png)

When the `combination` list is empty, the combination has been completed and the lock opens.
