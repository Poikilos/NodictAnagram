#!/usr/bin/env python
""" generated source for module ByteArrayFilter """
from __future__ import print_function
# package: com.somethingsimilar.opposite_of_a_bloom_filter
#
#  * ByteArrayFilter is used to filter out duplicate byte arrays from a given dataset or stream. It is
#  * guaranteed to never return a false positive (that is, it will never say that an item has already
#  * been seen by the filter when it has not) but may return a false negative.
#  *
#  * ByteArrayFilter is thread-safe.
#
class ByteArrayFilter(object):
    """ generated source for class ByteArrayFilter """
    HASH_FUNC = Hashing.murmur3_32()
    sizeMask = int()
    array = None
    MAX_SIZE = 1 << 30

    #
    #    * Constructs a ByteArrayFilter with an underlying array of the given size, rounded up to the next
    #    * power of two.
    #    *
    #    * This rounding occurs because the hashing is much faster on an array the size of a power of two.
    #    * If you really want a different sized array, used the AtomicReferenceArray constructor.
    #    *
    #    * @param size The size of the underlying array.
    #
    def __init__(self, size):
        """ generated source for method __init__ """
        if size <= 0:
            raise IllegalArgumentException("array size must be greater than zero, was " + size)
        if size > self.MAX_SIZE:
            raise IllegalArgumentException("array size may not be larger than 2**31-1, but will be rounded to larger. was " + size)
        #  round to the next largest power of two
        poweredSize = Intpow(2, Intlog2(size, RoundingMode.CEILING))
        self.sizeMask = poweredSize - 1
        self.array = AtomicReferenceArray(poweredSize)

    #
    #    * Returns whether the given byte array has been previously seen by this array. That is, if a byte
    #    * array with the same bytes as id has been passed to to this method before.
    #    *
    #    * This method may return false when it has seen an id before. This occurs if the id passed in
    #    * hashes to the same index in the underlying array as another id previously checked. On the
    #    * flip side, this method will never return true incorrectly.
    #    *
    #    * @param id The byte array that may have been previously seen.
    #
    def containsAndAdd(self, id):
        """ generated source for method containsAndAdd """
        code_ = self.HASH_FUNC.hashBytes(id)
        index = abs(code_.asInt()) & self.sizeMask
        oldId = self.array.getAndSet(index, id)
        return Arrays == id, oldId

    #
    #    * Returns the size of the underlying array. Welp.
    #    *
    #    * @return The size of the underlying array.
    #
    def getSize(self):
        """ generated source for method getSize """
        return len(array)

ByteArrayFilter.#    * @return Whether the byte array is contained in the ByteArrayFilter.

