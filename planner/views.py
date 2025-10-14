from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TripForm, ReviewForm
from .models import Trip, Review
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


def signup_view(request):
    """
    Handles user registration (sign up).
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
        if password != confirm_password:
            messages.error(request, "❌ Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠ Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠ Email already registered.")
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "✅ Account created successfully! You can now log in.")
        return redirect('login')

    return render(request, 'registration/signup.html')

def login_view(request):
    """
    Handles user authentication (login).
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "❌ Invalid username or password.")
            return redirect('login')

    return render(request, 'registration/login.html')



@login_required
def home_view(request):
   public_trips = Trip.objects.filter(is_public=True).order_by('-created_at')
   review_form = ReviewForm()
   return render(request,'home.html', {'public_trips': public_trips, 'review_form': review_form})

def mytrips_view(request):
    my_trips = Trip.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'trip/my_trip.html', {'my_trips': my_trips})


def public_trips(request):
    trips = Trip.objects.filter(is_public=True).order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        trip_id = request.POST.get('trip_id')
        trip = get_object_or_404(Trip, id=trip_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.trip = trip
            review.user = request.user
            review.save()
            return redirect('public_trips')
    else:
        form = ReviewForm()

    return render(request, 'trip/public_trips.html', {
        'public_trips': trips,
        'form': form
    })


@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('public_trips')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'trip/update_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect('public_trips')
    
    return render(request, 'trip/delete_review.html',{'review': review})


@login_required
def add_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect('home')
    else:
        form = TripForm()
    
    return render(request, "trip/add_trip.html",{'form': form})

class TripUdateView(UpdateView):
    model = Trip
    fields = ['title', 'budget', 'destination', 'start_date', 'end_date', 'description', 'is_public']
    template_name = 'trip/trip_form.html'
    success_url = reverse_lazy('my_trips')

class TripDeleteView(DeleteView):
    model = Trip
    template_name ='trip/trip_confirm_delete.html'
    success_url = reverse_lazy('my_trips')

def logout_view(request):
    """
    Logs out the current user and redirects to login page.
    """
    logout(request)
    messages.info(request, "👋 You have been logged out.")
    return redirect('login')
