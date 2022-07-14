import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConvertimgComponent } from './convertimg.component';

describe('ConvertimgComponent', () => {
  let component: ConvertimgComponent;
  let fixture: ComponentFixture<ConvertimgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConvertimgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConvertimgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
